import json
import os

class Task:

    """
    Represents a single task.
    """
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        """
        Convert Task object to dictionary for saving.
        """
        return {"title": self.title, "completed": self.completed}

    @staticmethod
    def from_dict(data):

        """
        Create Task object from dictionary.
        """
        return Task(data["title"], data["completed"])


class TaskManager:

    """
    Manages all tasks and handles file persistence.
    """
    def __init__(self, filename="tasks.json"):

        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, title):

        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()

        print("✅ Task added successfully!")

    def view_tasks(self):

        if not self.tasks:
            print("No tasks available.")
            return
        
        print("\nYour Tasks:")

        for idx, task in enumerate(self.tasks, start=1):

            status = "✔ Done" if task.completed else "❌ Pending"
            print(f"{idx}. {task.title} - {status}")

    def complete_task(self, task_number):

        if 0 < task_number <= len(self.tasks):

            self.tasks[task_number - 1].mark_completed()
            self.save_tasks()
            print("🎉 Task marked as completed!")

        else:
            print("Invalid task number.")

    def delete_task(self, task_number):

        if 0 < task_number <= len(self.tasks):

            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"🗑 Task '{removed_task.title}' deleted!")

        else:
            print("Invalid task number.")

    def save_tasks(self):

        """
        Save tasks to JSON file.
        """
        data = [task.to_dict() for task in self.tasks]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_tasks(self):
        """
        Load tasks from JSON file if it exists.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]


def show_menu():

    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    
    manager = TaskManager()  # Loads tasks from file automatically

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.view_tasks()
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                manager.complete_task(task_number)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        elif choice == "4":
            manager.view_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                manager.delete_task(task_number)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option. Please try again.")


main() # Start program
