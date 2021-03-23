import os.path
import json
from datetime import datetime

FILE_NAME = 'lists.json'

def show_lists(args):
  with open(FILE_NAME, 'r') as lists_json:
    try:
      data = json.load(lists_json)
      print("SNo.   Title     Priority  Due Date    Description")
      for index, todo_list in enumerate(data.keys()):
        print(index + 1,"    ",data[todo_list]['title'],"    ",data[todo_list]['priority'],"    ",data[todo_list]['due_date'],"  ",data[todo_list]['desc'])
    except:
      print('Some error occurred!')

def use_list(args):
  list_name = args[0]
  with open(FILE_NAME, 'r') as lists_json:
    try:
      data = json.load(lists_json)
      if (data.get(list_name)):
        return f'{list_name}.json'
      else:
        return -1
    except:
      print('Some error occurred!')

def create_list(args):
  list_name = args[0]
  # print(os.path.abspath('.'))
  new_list = {}
  with open(FILE_NAME, 'r+') as lists_json:
    try:
      data = json.load(lists_json)
      # print(data)
      # check if file already exists
      if (data.get(list_name)):
        print('List already exists! Try a different name...')
      else:

        # update the new_list dict

        desc = input('Enter description for the list : ')
        due_date =  input("Enter due date in YYYY-MM-DD for the list : ")   
        priority  = int(input('Enter priority : 1 being the lowest and 5 being the highest :'))
        new_list = {
        'title': list_name,
        'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'desc' : desc,
        'due_date' : due_date,
        'priority' : priority
        }
        data[list_name] = new_list
        with open(f'lists/{list_name}.json', 'w') as new_list:
          new_list.write(f'[\n]')
          print('Successfully created the new list!')
        # add to the lists.json
        lists_json.seek(0)
        json.dump(data, lists_json, sort_keys=True, indent=True)
    except:
      print('Some error occurred!')