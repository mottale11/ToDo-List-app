# base code
new_task = input("Enter the task: ")
todo_list.append(new_task)
print(f"{new_task} added")
if len(todo_list) == 0:
  print("Your ToDo list is empty")
else:
  len(todo_list) > 0
  index = 1
  for task in todo_list:
    print(f"{index}. {task}")
    index +=1
