class Task:
    """Base class for general tasks"""
    def __init__(self, title, description, deadline, task_type, status):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = status
        self.task_type = task_type

    def display_task_info(self):
        return (f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Deadline: {self.deadline}\n"
                f"Status: {self.status}\n"
                f"Type: {self.task_type}")

    def get_task_type(self):
        return "General Task"


class PersonalTask(Task):
    """Task subclass for personal tasks"""
    def __init__(self, title, description, deadline, task_type, status, category):
        super().__init__(title, description, deadline, task_type, status)
        self.category = category

    def display_task_info(self):
        base_info = super().display_task_info()
        return f"{base_info}\nCategory: {self.category}"

    def get_task_type(self):
        return "Personal Task"


class WorkTask(Task):
    """Task subclass for work-related tasks"""
    def __init__(self, title, description, deadline, task_type, status, priority):
        super().__init__(title, description, deadline, task_type, status)
        self.priority = priority

    def display_task_info(self):
        base_info = super().display_task_info()
        return f"{base_info}\nPriority: {self.priority}"

    def get_task_type(self):
        return "Work Task"


class TaskManager:
    """Class to manage tasks"""
    def __init__(self):
        self.db = []

    def add_new_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        task_type = input("Enter task type (personal/work/general): ").lower()
        status = input("Enter status: ")

        if task_type == "personal":
            category = input("Enter task category: ")
            new_task = PersonalTask(title, description, due_date, task_type, status, category)
        elif task_type == "work":
            priority = input("Enter task priority: ")
            new_task = WorkTask(title, description, due_date, task_type, status, priority)
        else:
            new_task = Task(title, description, due_date, task_type, status)

        self.db.append(new_task)
        print("Task added successfully!")

    def delete_task(self, title):
        for task in self.db:
            if task.title == title:
                self.db.remove(task)
                print("Task removed successfully!")
                return
        print("Task not found.")

    def show_task_list(self):
        if not self.db:
            print("No tasks available.")
            return
        print("\n--- Task List ---")
        for task in self.db:
            print(task.display_task_info())
            print("-" * 30)

    def update_due_date(self, title, new_due_date):
        for task in self.db:
            if task.title == title:
                task.deadline = new_due_date
                print("Due date updated successfully!")
                return
        print("Task not found.")

    def mark_task_completed(self, title):
        for task in self.db:
            if task.title == title:
                new_status = input("Enter new status (completed/quit): ").lower()
                if new_status in ("completed", "quit"):
                    task.status = new_status
                    print("Status updated successfully!")
                else:
                    print("Invalid status. Use 'completed' or 'quit'.")
                return
        print("Task not found.")


def menu(task_manager):
    while True:
        print("\n=== Task Manager ===")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Show all tasks")
        print("4. Update due date")
        print("5. Mark task as completed")
        print("6. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            task_manager.add_new_task()
        elif choice == "2":
            title = input("Enter the task title to remove: ")
            task_manager.delete_task(title)
        elif choice == "3":
            task_manager.show_task_list()
        elif choice == "4":
            title = input("Enter the task title to update: ")
            new_due_date = input("Enter the new due date: ")
            task_manager.update_due_date(title, new_due_date)
        elif choice == "5":
            title = input("Enter the task title to mark completed: ")
            task_manager.mark_task_completed(title)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    task_manager = TaskManager()
    menu(task_manager)
