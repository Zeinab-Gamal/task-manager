class Task:
    def __init__(self, title, description, deadline, task_type, status):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = status
        self.task_type = task_type

    def display_task_info(self):
        return f"title: {self.title}\ndescription: {self.description}\ndeadline: {self.deadline}\nstatus: {self.status}\ntype: {self.task_type}"

    def get_task_type(self):
        return "General Task"

class PersonalTask(Task):
    def __init__(self, title, description, deadline, task_type, status, category):
        super().__init__(title, description, deadline, task_type, status)
        self.category = category

    def display_info(self):
        base_info = super().display_task_info()
        return f"{base_info}\ncategory is {self.category} task type: {self.task_type}"

    def get_task_type(self):
        return "Personal Task"

class WorkTask(Task):
    def __init__(self, title, description, deadline, status, task_type, priority):
        super().__init__(title, description, deadline, task_type, status)
        self.priority = priority

    def display_info(self):
        base_info = super().display_task_info()
        return f"{base_info}\nPriority: {self.priority} task Type: {self.task_type}"

    def get_task_type(self):
        return "Work Task"

class TaskManager:
    def __init__(self):
        self.db = []

    def add_new_task(self):
        title = input("enter task title:")
        description = input("enter task description:")
        due_date = input("enter due date:")
        task_type = input("enter task type:")
        status = input("enter status:")

        if task_type == "personal":
            category = input("Enter task category: ")
            new_task = PersonalTask(title, description, due_date, task_type, status, category)
        elif task_type == "work":
            priority = input("Enter task priority: ")
            new_task = WorkTask(title, description, due_date, status, task_type, priority)
        else:
            new_task = Task(title, description, due_date, task_type, status)

        self.db.append(new_task)
        print("task added successfully!")

    def delete_task(self, title):
        for task in self.db:
            if task.title == title:
                self.db.remove(task)
                print("Task removed successfully!")
                break
        else:
            print("Title not found.")

    def show_task_list(self):
        try:
            num = int(input("enter the number of tasks you want to show: "))
        except ValueError:
            print("Invalid input Please enter a valid number.")
            return
        for i in range(num):
            title = input("enter the title of the task to show: ")
            for task in self.db:
                if task.title == title:
                    print(task.display_task_info())
                    break
            else:
                print(f"Task with title '{title}' not found.")

    def update_due_date(self, title, new_due_date):
        for task in self.db:
            if task.title == title:
                task.deadline = new_due_date
                print("Due date updated successfully!")
                break
        else:
            print("Title not found.")

    def mark_task_completed(self, title):
        for task in self.db:
            if task.title == title:
                status = input("enter the new status for the task (completed, quit) only: ")
                if status == "completed" or status == "quit":
                    task.status = status
                    print("Status updated successfully")
                else:
                    print("Please enter only 'completed' or 'quit'")
                break
        else:
            print("Title not found.")

def menu(task_manager):
    while True:
        print("\nEnter 1: Add a task\n2: Delete a task\n3: Show list of tasks\n4: Update due date\n5: Mark task as completed\n6: exit")

        user = input("Your choice: ")

        if user == "1":
            task_manager.add_new_task()

        elif user == "2":
            title = input("Enter the title of the task to remove: ")
            task_manager.delete_task(title)

        elif user == "3":
            task_manager.show_task_list()

        elif user == "4":
            title = input("Enter the title of the task to update due date: ")
            new_due_date = input("Enter the new due date: ")
            task_manager.update_due_date(title, new_due_date)

        elif user == "5":
            title = input("Enter the title of the task to mark as completed: ")
            task_manager.mark_task_completed(title)

        elif user == "6":
            print("Goodbye!")
            break

        else:
            print("Enter a valid number")

task1 = TaskManager()
menu(task1)
