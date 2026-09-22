tasks = [] 

while True:
    print("\nTodo List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    elif choice == '2':
        if tasks:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks found.")
    elif choice == '3':
        if tasks:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to remove.")
    elif choice == '4':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")
