from typing import List

class Task:
    def __init__(self, name: str, status: str = "Pending"):
        self.name = name
        self.status = status

    def __str__(self):
        return f"{self.name} - {self.status}"

class TodoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task_name: str) -> None:
        """Add a new task to the to-do list."""
        # Check if the task already exists
        for task in self.tasks:
            if task.name == task_name:
                return  # Task already exists, do nothing
        self.tasks.append(Task(task_name))

    def list_tasks(self) -> str:
        """Return a formatted string of all task names with their status."""
        if not self.tasks:
            return ""
        return  "Tasks:\n".join(f"- {task.name} - {task.status}" for task in self.tasks)

    def mark_task_completed(self, task_name: str) -> None:
        """Mark a task as completed."""
        for task in self.tasks:
            if task.name == task_name:
                task.status = "Completed"
                break

    def clear_tasks(self) -> None:
        """Clear all tasks from the to-do list."""
        self.tasks.clear()

    # Remove or comment out the persistence methods
    # def save_to_file(self, filename: str) -> None:
    #     """Save the tasks to a JSON file."""
    #     with open(filename, 'w') as file:
    #         json.dump([task.__dict__ for task in self.tasks], file)

    # def load_from_file(self, filename: str) -> None:
    #     """Load tasks from a JSON file."""
    #     try:
    #         with open(filename, 'r') as file:
    #             tasks = json.load(file)
    #             self.tasks = [Task(task['name'], task['status']) for task in tasks]
    #     except FileNotFoundError:
    #         self.tasks = []
