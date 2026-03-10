# # Task Manager CLI Application
# # Day 3 Project

# tasks = []


# def show_menu():
#     print("\n===== TASK MANAGER =====")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Complete Task")
#     print("4. Delete Task")
#     print("5. Exit")


# def add_task():
#     title = input("Enter task title: ")

#     task = {
#         "title": title,
#         "completed": False
#     }

#     tasks.append(task)

#     print("✅ Task added successfully!")


# def view_tasks():

#     if len(tasks) == 0:
#         print("No tasks available.")
#         return

#     print("\nYour Tasks:")

#     for index, task in enumerate(tasks, start=1):

#         status = "✔ Done" if task["completed"] else "❌ Pending"

#         print(f"{index}. {task['title']} - {status}")


# def complete_task():

#     view_tasks()

#     task_number = int(input("Enter task number to mark as completed: "))

#     if 0 < task_number <= len(tasks):

#         tasks[task_number - 1]["completed"] = True

#         print("🎉 Task marked as completed!")

#     else:
#         print("Invalid task number.")


# def delete_task():

#     view_tasks()

#     task_number = int(input("Enter task number to delete: "))

#     if 0 < task_number <= len(tasks):

#         removed_task = tasks.pop(task_number - 1)

#         print(f"🗑 Task '{removed_task['title']}' deleted!")

#     else:
#         print("Invalid task number.")


# def main():

#     while True:

#         show_menu()

#         choice = input("Choose an option: ")

#         if choice == "1":
#             add_task()

#         elif choice == "2":
#             view_tasks()

#         elif choice == "3":
#             complete_task()

#         elif choice == "4":
#             delete_task()

#         elif choice == "5":
#             print("Goodbye 👋")
#             break

#         else:
#             print("Invalid option. Please try again.")


# # Start program
# main()

# Task Manager CLI Application
# Day 3 Project

# tasks = []

# def show_menu():
#     print("\n===== TASK MANAGER =====")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Complete Task")
#     print("4. Delete Task")
#     print("5. Exit")

# def add_task():
#     title = input("Enter task title: ")

#     task = {
#         "title": title,
#         "completed": False
#     }

#     tasks.append(task)

#     print("✅ Task added successfully!")

#     # Show updated list
#     view_tasks()
#     print(f"updated list : {tasks}") 

# def view_tasks():

#     if len(tasks) == 0:
#         print("No tasks available.")
#         return

#     print("\nYour Tasks:")

#     for index, task in enumerate(tasks, start=1):

#         status = "✔ Done" if task["completed"] else "❌ Pending"

#         print(f"{index}. {task['title']} - {status}")

# def complete_task():

#     view_tasks()

#     try:
#         task_number = int(input("Enter task number to mark as completed: "))
#     except ValueError:
#         print("❌ Invalid input! Please enter a number.")
#         return

#     if 0 < task_number <= len(tasks):

#         tasks[task_number - 1]["completed"] = True

#         print("🎉 Task marked as completed!")

#         # Show updated list
#         view_tasks()
#         print(f"updated list : {tasks}") 

#     else:
#         print("Invalid task number.")

# def delete_task():

#     view_tasks()

#     try:
#         task_number = int(input("Enter task number to delete: "))
#     except ValueError:
#         print("❌ Invalid input! Please enter a number.")
#         return

#     if 0 < task_number <= len(tasks):

#         removed_task = tasks.pop(task_number - 1)

#         print(f"🗑 Task '{removed_task['title']}' deleted!")

#         # Show updated list
#         view_tasks()
#         print(f"updated list : {tasks}")  

#     else:
#         print("Invalid task number.")

# def main():

#     while True:

#         show_menu()

#         choice = input("Choose an option: ")

#         if choice == "1":
#             add_task()

#         elif choice == "2":
#             view_tasks()

#         elif choice == "3":
#             complete_task()

#         elif choice == "4":
#             delete_task()

#         elif choice == "5":
#             print("Goodbye 👋")
#             break

#         else:
#             print("Invalid option. Please try again.")

# # Start program
# main()






# Task Manager CLI Application
# Day 3 Project

tasks = []

def show_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task title: ")

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)

    print("✅ Task added successfully!")

    # Show updated list
    view_tasks()
    print(f"updated list : {tasks}") 

def view_tasks():

    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\nYour Tasks:")

    for index, task in enumerate(tasks, start=1):

        status = "✔ Done" if task["completed"] else "❌ Pending"

        print(f"{index}. {task['title']} - {status}")

def complete_task():

    view_tasks()

    try:
        task_number = int(input("Enter task number to mark as completed: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    if 0 < task_number <= len(tasks):

        tasks[task_number - 1]["completed"] = True

        print(f"🎉{task['title']} Task marked as completed!")

        # Show updated list
        view_tasks()
        print(f"updated list : {tasks}") 

    else:
        print("Invalid task number.")

def delete_task():

    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    if 0 < task_number <= len(tasks):

        removed_task = tasks.pop(task_number - 1)

        print(f"🗑 Task '{removed_task['title']}' is deleted!")

        # Show updated list
        view_tasks()
        print(f"updated list : {tasks}")  

    else:
        print("Invalid task number.")

def main():

    while True:

        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option. Please try again.")

# Start program
main()
