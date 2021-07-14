# Task Manager

## What the program does:
This program allows teams to assign, keep track of, make changes to, and generate reports about tasks. In short, it is a task management app. It handles data persistence by storing data in text files and then accessing those files to make changes to the data they store. The program has different levels of functionality depending on the type of user who logs into it. Once regular users are logged in, the program allows them to add new tasks, view all tasks, and view the tasks assigned to them specifically. If the user who logs in has admin privileges, they can use the program to register new users, add tasks, view all tasks, view their tasks, and generate as well as view reports about the tasks.

## How the code works:
Diving into the code of this program, the developer will find that it uses functions to handle registering users, adding tasks, finding and filtering tasks, and generating reports. These functions appear at the top of the file. Most of these functions access two files, 'user.txt' and 'tasks.txt', convert the data they contain into lists and dictionaries as a way of cleaning it, search through it, and in some cases make changes to that data before writing these changes back into the files. In the case of the 'generate_reports' and 'view_stats' functions, the two files mentioned above get used to generate two new files, 'task_overview.txt' and 'user_overview.txt'. After the functions, the developer will find the code for logging in that checks whether the user has a valid username and password when the program gets run. The final piece of code gives the user a series of choices, provided they logged in successfully and then handles the implementation of the above functions based on the choice the user made.

## Running the program.
To run this program:
1. Download the files in this repository and store them in a folder of your choice,
2. open the 'task_manager.py' file in IDLE,
3. run the program,
4. you will then be presented with a menu for logging in,
5. after logging in, you can then use the features of the program described above.

