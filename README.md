Daily Task Planner
Introduction:
The daily task planner is a command line interface (CLI) application that allows users to manage their daily tasks. This CLI application is perfect for anyone who wants a simple and easy to manage their daily tasks without the complexity of a full-fledged project management tool. This application supports the adding new tasks with description and optional dates, viewing tasks with optional filtering by date, marking tasks as completed and deleting tasks. The current implementation assumes that all tasks are uniquely identified by their ID.
All the tasks are saved in a JSON file, so they stay even after users close the application. This makes it easy to resume task management whenever needed.

Key Features:
•	Adding New Tasks: 
Users can easily add tasks with descriptions and optional due dates. If no date is provided, the task will be saved with "None" as the date in the task list. This approach makes the application flexible for various use cases.
•	Viewing Tasks: 
Users can view all tasks without adding the date. And users can filter the list of the task by a specific date which helps to focus on the tasks of a particular day.
•	Marking Tasks as Completed: 
Once a task is finished or completed, users can mark it as a completed that helps to track progress and stay organized.
•	Deleting Tasks: 
Unnecessary and completed tasks can be deleted to maintain an up-to-date task list.

Technologies Used:
•	Python: This application is build using python3. ( Python official documentation)
•	JSON: Task data is stored in a JSON file for persistent storage. (Json Documentation)
•	No additional libraries need to be installed for this code to run. The code exclusively uses Python's built-in libraries.

Installation Instructions:
This provides clarity of the application and ensures users can follow each step without confusion.
1. Clone the Repository
•	To get started, clone the repository to your local machine. Use the following command in your terminal or command prompt: (For more details, refer to Git documentation.)
Command: git clone <repository_url>
2. Install Python
•	Ensure you have Python 3.x installed on your machine. You can download it from the official Python website: https://www.python.org.
•	Verify the installation by running:
Command: python –version, python3 –version

4. Run the Application
•	Navigate to the folder containing the project files:
Command: cd <project_folder_name>
•	Run the application using the command:
Command: python <filename>.py or python3 <filename>.py
How to Use?
Once the program is running, users will be presented with a menu of options to interact with the application. Here is the screenshot of the menu options: (CLI Documentation)

1.	Add a Task:
Enter 1 to add task, enter a description for the task and an optional date (in the format YYYY-MM-DD).

2.	View Tasks:
Enter 2 to view all tasks list and users can filter tasks by date (in the format YYYY-MM-DD).

3.	Mark a Task as Done:
Enter 3 to mark tasks as done, users will be prompted to enter the task ID you wish to mark as done.
 

4.	Delete a Task:
Enter 4, users will be prompted to enter the task ID you wish to delete.
 
5.	Exit:
Enter 5, users can be exit from the app.
 
Code Explanation and Inline Comments:
Below is the snippet of the code for the Daily Task Planner application with detailed inline comments to explain its functionality.
 

Test Cases:
1.	Adding tasks with/without dates and handling invalid dates.
a.	Adding task with valid date with successfully added task.
 

b.	Adding task without date, a warning will inform users that the task is being added without a date.
 

c.	Adding task with the past date, another warning message will be informed users that the date is in the past, but the task is still added.
 
2.	Viewing tasks list with/without valid dates and handling invalid dates
a.	Viewing all tasks list without adding date
 
b.	Viewing all tasks with a valid date
 
c.	Viewing all tasks without a valid date
 

3.	Marked task as completed with/without valid id and handling invalid id.
a.	Marked task as completed with valid task id.
 
b.	Marked task as completed with invalid task id.
 

4.	Delete task with/without valid task id and handling invalid id.
a.	Delete task with valid id
 

b.	Try to delete task with invalid id
 

5.	Exit 
 


Conclusion:
In conclusion, the Daily Task Planner is a simple and effective tool for managing daily tasks. Its well-organized code makes it easy to add, view, mark, and delete tasks. Tasks are saved in a JSON file, so they remain available even after the program is closed. The application also includes basic error handling to guide users and ensure it runs smoothly, even if mistakes are made.
 
