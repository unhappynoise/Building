import json
import os.path


class Task:
    def __init__(self, name, completed = False):
        self.name = name
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "√" if self.completed else "X"
        return f"{status} {self.name}"

class TaskManager:
    def __init__(self, filename = 'task.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return [Task(**task) for task in json.load(f)]
        return []

    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)
        self.save_tasks()
        is_completed = input(f"Is the task '{name}' completed? (yes or no): ").strip().lower()
        if is_completed == 'yes':
            task.mark_completed()
            print(f"Task '{name}' marked as completed.")
        else:
            print(f"Task '{name}' added as incomplete.")

        self.save_tasks()

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def view_tasks(self):
        print("Tasks:")
        for task_name, task in enumerate(self.tasks):
            status = "√" if task.completed else "X"
            print(f"{task_name + 1} : {task.name} [{status}]")

    def mark_completed(self, task_name):
        for task in self.tasks:
            if task.name.lower() == task_name.lower():
                task.mark_completed()
                self.save_tasks()
                print(f"Task '{task_name}' marked as completed.")
                return
        print(f"Task '{task_name}' not found.")

    def delete_task(self, task_name):
        task_to_delete = next((task for task in self.tasks if task.name.lower() == task_name.lower()), None)
        if task_to_delete:
            self.tasks.remove(task_to_delete)
            print(f"Task '{task_name}' deleted.")
            self.save_tasks()
        else:
            print(f"Task '{task_name}' not found.")

def main():
    manager = TaskManager()
    while True:
        command = input("Enter a command (add/view/delete/complete/exit): ").strip().lower()
        if command == 'add':
            name = input("Enter task name: ")
            manager.add_task(name)

        elif command == 'view':
            manager.view_tasks()

        elif command == 'delete':
            task_name = str(input("Enter name of task to be deleted: "))
            manager.delete_task(task_name)

        elif command == 'complete':
            task_name = str(input("Enter name of task to be completed: "))
            manager.mark_completed(task_name)

        elif command == 'exit':
            break

    else:
        print("Invalid command! Try agian.")

if __name__ == "__main__":
    main()
