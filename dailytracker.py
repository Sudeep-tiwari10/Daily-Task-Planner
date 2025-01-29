# Import necessary libraries
import json  # For handling JSON data (reading, writing, parsing)
import os  # For checking file existence and file operations
from datetime import datetime  # For working with dates and times

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from the JSON file
def load_tasks():
    # If the file doesn't exist, return an empty list
    if not os.path.exists(TASK_FILE):
        return []
    # Open the file in read mode and load JSON data
    with open(TASK_FILE, "r") as file:
        return json.load(file)

# Save tasks to the JSON file
def save_tasks(tasks):
    # Open the file in write mode and save JSON data with indentation
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description, date=None):
    # Load existing tasks
    tasks = load_tasks()
    warning = None  # Initialize a warning message (if any)

    if date:
        try:
            # Validate and parse the date input
            due_date = datetime.strptime(date, "%Y-%m-%d").date()
            # Check if the date is in the past and set a warning if necessary
            if due_date < datetime.now().date():
                warning = "Warning: The date is in the past. Task added anyway."
        except ValueError:
            # Handle invalid date format
            print("Invalid date format. Use 'YYYY-MM-DD'.")
            return
    else:
        # Set a warning if no date is provided
        warning = "Warning: Task added without a date."

    # Create a new task dictionary
    task = {
        "id": len(tasks) + 1,  # Assign a unique ID based on the number of tasks
        "description": description,  # Task description
        "date_time": date if date else None,  # Task date or None if not provided
        "status": "Pending"  # Default status is 'Pending'
    }

    # Append the new task to the task list
    tasks.append(task)
    # Save the updated task list to the file
    save_tasks(tasks)

    print("Task added successfully.")
    if warning:
        print(warning)

# View tasks (optionally filtered by date)
def view_tasks(date=None):
    # Load all tasks
    tasks = load_tasks()

    if date:
        try:
            # Validate and parse the filter date
            filter_date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            # Handle invalid date format
            print("Invalid date format. Use 'YYYY-MM-DD'.")
            return

        # Filter tasks that match the specified date
        tasks = [
            task for task in tasks
            if task.get("date_time") and datetime.strptime(task["date_time"], "%Y-%m-%d").date() == filter_date
        ]

    # If no tasks are found, display a message
    if not tasks:
        print("No tasks found.")
        return

    # Display tasks with their details
    print("Tasks:")
    for task in tasks:
        date_time = task.get('date_time', 'No date')  # Handle missing 'date_time'
        print(f"[{task['id']}] {task['description']} | Date: {date_time} | Status: {task['status']}")

# Mark a task as done
def mark_task_done(task_id):
    # Load all tasks
    tasks = load_tasks()

    # Find the task by its ID and mark it as completed
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed.")
            return

    # If the task is not found, display a message
    print("Task not found.")

# Delete a task
def delete_task(task_id):
    # Load all tasks
    tasks = load_tasks()

    # Find the task by its ID and remove it from the list
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            return

    # If the task is not found, display a message
    print("Task not found.")

# Display the main menu
def display_menu():
    print("\nDaily Task Planner")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

# Main function to run the program
def main():
    while True:
        # Display the menu options
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new task
            description = input("Enter task description: ")
            date = input("Enter date (YYYY-MM-DD) or leave blank: ")
            add_task(description, date if date else None)

        elif choice == "2":
            # View tasks (optionally filtered by date)
            date = input("Enter a date to filter tasks (YYYY-MM-DD) or leave blank to view all: ")
            view_tasks(date if date else None)

        elif choice == "3":
            try:
                # Mark a task as done
                task_id = int(input("Enter the task ID to mark as done: "))
                mark_task_done(task_id)
            except ValueError:
                # Handle invalid input for task ID
                print("Invalid task ID. Please enter a number.")

        elif choice == "4":
            try:
                # Delete a task
                task_id = int(input("Enter the task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                # Handle invalid input for task ID
                print("Invalid task ID. Please enter a number.")

        elif choice == "5":
            # Exit the program
            print("Exiting the Daily Task Planner. Goodbye!")
            break

        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
