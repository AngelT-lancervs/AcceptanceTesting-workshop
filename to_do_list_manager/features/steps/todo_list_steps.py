# features/steps/todo_list_steps.py
from behave import given, when, then
from todo_list import TodoList

# Initialize an instance of TodoList for testing
todo_list = TodoList()

@given('the to-do list is empty')
def step_impl(context):
    todo_list.clear_tasks()

@given('the to-do list contains tasks')
def step_impl(context):
    todo_list.clear_tasks()  # Clear existing tasks
    for row in context.table:
        task_name = row['Task']
        todo_list.add_task(task_name)

@when('the user adds a task "{task_name}"')
def step_impl(context, task_name):
    todo_list.add_task(task_name)

@when('the user lists all tasks')
def step_impl(context):
    context.result = todo_list.list_tasks()

@when('the user marks task "{task_name}" as completed')
def step_impl(context, task_name):
    todo_list.mark_task_completed(task_name)

@when('the user clears the to-do list')
def step_impl(context):
    todo_list.clear_tasks()

@then('the to-do list should contain "{task_name}"')
def step_impl(context, task_name):
    tasks = todo_list.list_tasks()
    assert f"- {task_name} - Pending" in tasks, f"Task '{task_name}' not found in the list"

@then('the output should contain')
def step_impl(context):
    expected_output = context.text.strip().splitlines()
    actual_output = todo_list.list_tasks().strip().splitlines()

    # Add the 'Tasks:' header to the expected_output if it's not already present
    if expected_output[0] != "Tasks:":
        expected_output = ["Tasks:"] + expected_output

    # Print both expected and actual outputs for debugging
    print("Expected output:", expected_output)
    print("Actual output:", actual_output)

    # Check that both outputs have the same number of lines
    assert len(expected_output) == len(actual_output), f"Expected {len(expected_output)} lines but got {len(actual_output)}"

    # Compare each line of the expected and actual output
    for expected_line, actual_line in zip(expected_output, actual_output):
        assert expected_line.strip() == actual_line.strip(), f"Expected line: '{expected_line}' but got '{actual_line}'"

        
@then('the to-do list should show task "{task_name}" as completed')
def step_impl(context, task_name):
    tasks = todo_list.list_tasks()
    assert f"- {task_name} - Completed" in tasks, f"Task '{task_name}' is not marked as completed"

@then('the to-do list should be empty')
def step_impl(context):
    assert todo_list.list_tasks() == "", "The to-do list is not empty"

@then('the to-do list should still contain one "{task_name}"')
def step_impl(context, task_name):
    tasks = todo_list.list_tasks()
    task_count = sum(1 for task in tasks.splitlines() if task.startswith(f"- {task_name}"))
    assert task_count == 1, f"Task '{task_name}' appears {task_count} times"

@then('the to-do list should still show task "{task_name}" as pending')
def step_impl(context, task_name):
    tasks = todo_list.list_tasks()
    assert f"- {task_name} - Pending" in tasks, f"Task '{task_name}' is not shown as pending"
