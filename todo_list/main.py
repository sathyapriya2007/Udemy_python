tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 3:
        num = int(input("Enter task number to delete: "))
        if num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")