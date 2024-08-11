class Task:
    def __init__(self, title, description, priority, deadline):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Deadline: {self.deadline}, Status: {status}"


def add_task(task_list):
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    priority = input("Enter task priority (High/Medium/Low): ").strip().capitalize()
    deadline = input("Enter task deadline (YYYY-MM-DD): ").strip()

    task = Task(title, description, priority, deadline)
    task_list.append(task)
    print(f"Task '{title}' added successfully.")


def list_tasks(task_list):
    if not task_list:
        print("No tasks available.")
        return

    print("\nCurrent Tasks:")
    for i, task in enumerate(task_list, 1):
        print(f"{i}. {task}")
    print()


def update_task(task_list):
    if not task_list:
        print("No tasks available.")
        return

    list_tasks(task_list)
    try:
        task_number = int(input("Enter the task number you want to update: "))
        if task_number < 1 or task_number > len(task_list):
            print("Invalid task number.")
            return
        task = task_list[task_number - 1]
        new_title = input(f"Enter new title (current: {task.title}): ").strip()
        new_description = input(f"Enter new description (current: {task.description}): ").strip()
        new_priority = input(f"Enter new priority (current: {task.priority}): ").strip().capitalize()
        new_deadline = input(f"Enter new deadline (current: {task.deadline}): ").strip()

        task.title = new_title if new_title else task.title
        task.description = new_description if new_description else task.description
        task.priority = new_priority if new_priority else task.priority
        task.deadline = new_deadline if new_deadline else task.deadline

        print(f"Task '{task.title}' updated successfully.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(task_list):
    if not task_list:
        print("No tasks available.")
        return

    list_tasks(task_list)
    try:
        task_number = int(input("Enter the task number you want to delete: "))
        if task_number < 1 or task_number > len(task_list):
            print("Invalid task number.")
            return
        task = task_list.pop(task_number - 1)
        print(f"Task '{task.title}' deleted successfully.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    task_list = []
    while True:
        command = input("Enter a command (add/list/update/delete/exit): ").strip().lower()
        if command == "add":
            add_task(task_list)
        elif command == "list":
            list_tasks(task_list)
        elif command == "update":
            update_task(task_list)
        elif command == "delete":
            delete_task(task_list)
        elif command == "exit":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
