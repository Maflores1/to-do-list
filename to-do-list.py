import json

# File where the tasks will be saved
TASKS_FILE = 'tasks.json'

# Function to display the main menu


def print_menu():
    print('\nTodo List Menu:')
    print('1. View Tasks')  # Option to view all tasks
    print('2. Add a Task')  # Option to add a new task
    print('3. Remove a Task')  # Option to remove an existing task
    print('4. Mark a Task as Completed')  # Option to mark a task as completed
    print('5. View Completed Tasks')  # Option to view completed tasks
    print('6. Filter Tasks by Category')  # Option to filter tasks by category
    print('7. Exit')  # Option to exit the program

# Function to get the user's choice for the menu


def get_choice():
    while True:
        choice = input('Enter your choice: ')  # Prompt user for a choice
        valid_choices = ('1', '2', '3', '4', '5', '6', '7')  # Valid options
        if choice not in valid_choices:  # If the choice is invalid
            print('Invalid choice')
            continue
        else:
            return choice  # Return valid choice

# Function to display the tasks in the list


def display_tasks(tasks, completed=False, category=None):
    if not tasks:  # If the task list is empty
        print('No tasks in the list.')
        return

    # Filter tasks by completion status (completed or pending)
    if completed:
        print("\nCompleted Tasks:")
        tasks_to_display = [task for task in tasks if task['completed']]
    else:
        tasks_to_display = [task for task in tasks if not task['completed']]

    # If a category is specified, filter tasks by that category
    if category:
        tasks_to_display = [
            task for task in tasks_to_display if task['category'].lower() == category.lower()]

    # If no tasks to display after filtering, inform the user
    if not tasks_to_display:
        print('No tasks available.')
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks_to_display, start=1):
            # Display task with its status (completed or pending) and category
            status = "Completed" if task['completed'] else "Pending"
            print(f'{index}. {task["task"]} - {status} ({task["category"]})')

# Function to add a new task to the list


def add_task(tasks):
    while True:
        # Get task description from user
        task_description = input('Enter a new task: ').strip()
        if len(task_description) != 0:  # Ensure task is not empty
            category = input(
                'Enter the category for this task (e.g., Work, Personal): ').strip()  # Get category
            # Append new task as a dictionary with task description, completed status, and category
            tasks.append({"task": task_description,
                         "completed": False, "category": category})
            break
        else:
            print('Invalid task!')  # Prompt again if the task is empty

# Function to remove a task from the list


def remove_task(tasks):
    display_tasks(tasks)  # Show tasks before removing

    while True:
        try:
            # Get task number to remove
            task_number = int(input('Enter the task number to remove: '))
            if 1 <= task_number <= len(tasks):  # Check if task number is valid
                tasks.pop(task_number - 1)  # Remove the task
                break
            else:
                raise ValueError  # If task number is out of range, raise error
        except ValueError:
            # Prompt again if the input is invalid
            print('Invalid task number')

# Function to mark a task as completed


def mark_task_completed(tasks):
    display_tasks(tasks)  # Show tasks before marking completed

    while True:
        try:
            task_number = int(
                input('Enter the task number to mark as completed: '))  # Get task number
            if 1 <= task_number <= len(tasks):  # Check if task number is valid
                # Mark the task as completed
                tasks[task_number - 1]['completed'] = True
                break
            else:
                raise ValueError  # If task number is out of range, raise error
        except ValueError:
            # Prompt again if the input is invalid
            print('Invalid task number')

# Function to filter tasks by category (e.g., Work, Personal)


def filter_tasks_by_category(tasks):
    category = input(
        'Enter the category to filter by (e.g., Work, Personal): ').strip()  # Get category to filter by
    display_tasks(tasks, category=category)  # Display filtered tasks

# Function to load tasks from a file


def load_tasks():
    """Load tasks from a file"""
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)  # Read the tasks from the JSON file
    except (FileNotFoundError, json.JSONDecodeError):  # If file doesn't exist or is corrupt
        tasks = []  # Return an empty list if there's no file or it's empty
    return tasks  # Return the loaded tasks

# Function to save tasks to a file


def save_tasks(tasks):
    """Save tasks to a file"""
    with open(TASKS_FILE, 'w') as file:
        # Write tasks to the JSON file with indentation for readability
        json.dump(tasks, file, indent=4)

# Main function to run the todo list program


def main():
    tasks = load_tasks()  # Load tasks from the file when the program starts

    while True:
        print_menu()  # Display the main menu

        choice = get_choice()  # Get the user's menu choice

        # Execute different functions based on the user's choice
        if choice == '1':
            display_tasks(tasks)  # Option to view all tasks
        elif choice == '2':
            add_task(tasks)  # Option to add a new task
        elif choice == '3':
            remove_task(tasks)  # Option to remove a task
        elif choice == '4':
            mark_task_completed(tasks)  # Option to mark a task as completed
        elif choice == '5':
            # Option to view completed tasks
            display_tasks(tasks, completed=True)
        elif choice == '6':
            # Option to filter tasks by category
            filter_tasks_by_category(tasks)
        else:
            save_tasks(tasks)  # Option to save tasks before exiting
            print("Exiting and saving tasks...")  # Inform user tasks are saved
            break  # Exit the program


# Run the program
if __name__ == '__main__':
    main()
