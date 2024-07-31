import os
from todo_list import TodoList

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Print the main menu."""
    print("To-Do List Manager")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Clear all tasks")
    print("5. Exit")

def main():
    todo_list = TodoList()

    while True:
        clear_screen()
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            task_name = input("Enter task name: ").strip()
            if task_name:
                todo_list.add_task(task_name)
                print(f"Added task: {task_name}")
            else:
                print("Task name cannot be empty.")
        
        elif choice == '2':
            tasks = todo_list.list_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("Tasks:")
                print(tasks)  # Print the tasks directly
            input("Press Enter to continue...")
        
        elif choice == '3':
            task_name = input("Enter task name to mark as completed: ").strip()
            if task_name:
                todo_list.mark_task_completed(task_name)
                print(f"Marked task '{task_name}' as completed.")
            else:
                print("Task name cannot be empty.")
        
        elif choice == '4':
            todo_list.clear_tasks()
            print("Cleared all tasks.")
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        input("Press Enter to continue...")

if __name__ == '__main__':
    main()
