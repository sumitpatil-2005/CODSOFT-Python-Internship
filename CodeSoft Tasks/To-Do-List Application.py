# To-Do List Application

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    # View Tasks
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Add Task
    elif choice == "2":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    # Mark Task Completed
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num-1] = tasks[task_num-1] + " ✔"
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num-1)
                print(f"Task '{removed}' deleted.")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Exiting To-Do List App. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")