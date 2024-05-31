class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the list.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = new_task
            print(f'Task "{old_task}" updated to "{new_task}".')
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f'Task "{task}" deleted from the list.')
        else:
            print("Invalid task number.")


def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            to_do_list.add_task(task)
        elif choice == '2':
            to_do_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            to_do_list.update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            to_do_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()