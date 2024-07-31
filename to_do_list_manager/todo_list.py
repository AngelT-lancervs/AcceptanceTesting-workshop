from typing import List, Optional
from datetime import datetime

class Task:
    def __init__(self, name: str, status: str = "Pending", due_date: Optional[datetime] = None):
        self.name = name
        self.status = status
        self.due_date = due_date

    def __str__(self):
        due_date_str = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No due date"
        return f"{self.name} - {self.status} (Due: {due_date_str})"

class TodoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task_name: str, due_date: Optional[datetime] = None) -> None:
        """Add a new task to the to-do list with an optional due date."""
        # Check if the task already exists
        for task in self.tasks:
            if task.name == task_name:
                return  # Task already exists, do nothing
        self.tasks.append(Task(task_name, due_date=due_date))

    def list_tasks(self) -> str:
        """Return a formatted string of all task names with their status and due date."""
        if not self.tasks:
            return ""
        return  "Tasks:\n" + "\n".join(f"- {task.name} - {task.status} (Due: {task.due_date.strftime('%Y-%m-%d') if task.due_date else 'No due date'})" for task in self.tasks)

    def mark_task_completed(self, task_name: str) -> None:
        """Mark a task as completed."""
        for task in self.tasks:
            if task.name == task_name:
                task.status = "Completed"
                break

    def clear_tasks(self) -> None:
        """Clear all tasks from the to-do list."""
        self.tasks.clear()
