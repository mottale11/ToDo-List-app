# base code

todo_list = []

while True:
  if len(todo_list) == 0:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1


  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")
  
  choice = input("Enter choice (1, 2, or 3): ")

  if choice == "1":
    print(f"Adding task")
    new_task = input("Enter you task: ")
    todo_list.append(new_task)
    print("Your task has been added.")
  elif choice == "2":
    if len(todo_list) == 0:
      print("ToDo list is empty")
    elif len(todo_list) > 0:
      todo_list.pop()
  elif choice == "3":
    print("Quitting")
    break
