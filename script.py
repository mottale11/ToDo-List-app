# base code

todo_list = ["Watch a movie", "Take a walk", "Submit project work"]

while True:
  todo_list = ["Watch a movie", "Take a walk", ]
  
  # Ask users to add new task
  new_task = input("Enter the task: ")
  todo_list.append(new_task)     # adding the new task
  print(f"{new_task} added")
  if len(todo_list) == 0:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
