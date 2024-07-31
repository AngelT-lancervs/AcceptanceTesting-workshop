import pytest
from datetime import datetime
from todo_list import Task, TodoList  # Replace 'your_module' with the actual module name

def test_add_task():
    """Test adding a new task to the to-do list."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    
    # Check if the task was added
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].name == "Buy groceries"
    assert todo_list.tasks[0].status == "Pending"
    assert todo_list.tasks[0].due_date is None

def test_add_duplicate_task():
    """Test adding a duplicate task to ensure it is not added again."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Buy groceries")  # Attempt to add a duplicate task
    
    # Check if the duplicate was not added
    assert len(todo_list.tasks) == 1  # Only one task should be present

def test_list_tasks():
    """Test listing all tasks to ensure correct formatting and content."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Pay bills")
    
    # Expected output
    expected_output = (
        "Tasks:\n"
        "- Buy groceries - Pending (Due: No due date)\n"
        "- Pay bills - Pending (Due: No due date)"
    )
    
    # Check if the output matches the expected format
    assert todo_list.list_tasks().strip() == expected_output

def test_mark_task_completed():
    """Test marking a task as completed."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.mark_task_completed("Buy groceries")
    
    # Check if the task status is updated to 'Completed'
    assert todo_list.tasks[0].status == "Completed"

def test_clear_tasks():
    """Test clearing all tasks from the to-do list."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Pay bills")
    todo_list.clear_tasks()
    
    # Check if all tasks were cleared
    assert len(todo_list.tasks) == 0

def test_add_task_with_due_date():
    """Test adding a task with an optional due date."""
    todo_list = TodoList()
    due_date = datetime(2024, 12, 31)
    todo_list.add_task("Buy groceries", due_date)
    
    # Check if the task was added with the correct due date
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].due_date == due_date

# Add more tests as needed

