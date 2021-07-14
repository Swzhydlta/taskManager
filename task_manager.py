# Daniel Nel
# Capstone project III

# This is a task management program that allows users to log in and
# interact with tasks in various ways. It stores login details, task
# details,and reports in .txt files. It is able to access those files
# to read them, change them and display information from them.

from datetime import datetime

user_file = "user.txt"
task_file = "tasks.txt"

#****************************************************************
#****************************FUNCTIONS***************************

# Define functions for user registration, adding tasks, viewing tasks,
# viewing stats, and generating reports.


def reg_user(user_file):
    """Register a new user"""
    valid_new_username = False
    users = []
    # Ask for a new username and check if it exists already in user.txt.
    with open(user_file, "r+") as f:
        while valid_new_username == False:
            new_user_username = input("Please enter a username: ")
            for line in f:
                    listline = line.split()
                    file_username = listline[0].replace(",", "")
                    users.append(file_username)
            if new_user_username in users:
                    print("Sorry, a user with that name exists already.")
            else:
                valid_new_username = True

                
    # If not, ask for a password and confirm it.
    if valid_new_username == True:
        new_user_password1 = input("Please enter a password: ")
        new_user_password2 = input("Please confirm the password: ")
        while new_user_password1 != new_user_password2:
            new_user_password2 = input("Those passwords don't match. Please confirm the password: ")
        new_user_username += ","
        # Add new username to end of file.
        with open(user_file, "r+") as f:
            data = f.read(100) 
            if len(data) > 0 :
                f.write("\n")
                f.write(new_user_username)
                f.write(" ")
                f.write(new_user_password2)
    print("\nUser added!")


def add_task(task_file):
    """This function adds new tasks to tasks.txt"""
    # Get user input for all categories of the new task
    person = input("Username of taskholder: ")
    person += ", "
    task_title = input("Title of task: ")
    task_title += ", "
    task_description = input("Description of task: ")
    task_description += ", "
    due_date = input("Due date (e.g., 10 Oct 2021): ")
    due_date += ", "
    current_date = datetime.now() 
    current_date = current_date.strftime("%d %b %Y")
    current_date += ", "
    # Write data to file
    with open(task_file, "r+") as f:
        data = f.read(100) 
        if len(data) > 0 :
            f.write("\n")
            f.write(person)
            f.write(task_title)
            f.write(task_description)
            f.write(current_date)
            f.write(due_date)
            f.write("No")
    print("\nTask added!")

def view_all(task_file):
    """View all tasks"""
    # Look in the task file and print each one out in a formatted string.
    with open(task_file, "r+") as f:
        for line in f:
            list_line = line.split(",")
            list_line5 = list_line[5].replace("\n", "")
            print(f'''
Task:                {list_line[1]} 
Assigned to:          {list_line[0]}
Date assigned:       {list_line[3]}
Due date:            {list_line[4]}
Task complete?       {list_line5}
Task Description:
        {list_line[2]}''')


def view_mine(task_file):
    """This function allows the logged in user to view all tasks that
    pertain to them. It also lets the user edit the task in its task
    file by marking it as complete, changing the due date, or changing the
    user who the task is assigned to.
    """
    # Look in task file, build a list of tasks that belong to the user
    # and print it to the screen in a formatted string.
    running = True
    choice = 0
    while running:
        users_tasks = []
        with open(task_file, "r+") as f:
            for line in f:
                list_line = line.split(",")
                if username == list_line[0]:
                    list_line5 = list_line[5].replace("\n", "")
                    list_line.remove(list_line[5])
                    list_line.append(list_line5)
                    users_tasks.append(list_line)
        for i in range(0, len(users_tasks)):
            print(f'''
Task number:          {i+1}
Task:                {users_tasks[i][1]} 
Assigned to:          {users_tasks[i][0]}
Date assigned:       {users_tasks[i][3]}
Due date:            {users_tasks[i][4]}
Task complete?       {users_tasks[i][5]}
Task Description:
        {users_tasks[i][2]}''')

            
        # Ask the user to select a task from the list and display it
        # on the screen in a formatted string.
        task_chooser = True
        while task_chooser == True:
            choice = int(input("\n Select a task number to choose a task or press -1 to go back to main menu: "))
            # If user chose a valid task, print it to the screen.
            if choice > 0 and choice <= len(users_tasks):
                one_task = True
                if one_task == True:
                    print(f'''
Task number:          {choice}
Task:                {users_tasks[choice-1][1]} 
Assigned to:          {users_tasks[choice-1][0]}
Date assigned:       {users_tasks[choice-1][3]}
Due date:            {users_tasks[choice-1][4]}
Task complete?       {users_tasks[choice-1][5]}
Task Description:
        {users_tasks[choice-1][2]}''')

                    
                    # Ask the user if they want to edit the task, mark it as complete, or go back.
                    one_task_choice = input("\nPress 'c' to mark as complete, 'e' to edit, or 'b' to go back. ")
                    users_task = users_tasks[choice-1][1]
                    list_of_tasks = []
                    string_of_tasks = ""

                    # If user chose 'c', mark the task as complete by changing "No" to "Yes" in the list.
                    if one_task_choice == "c":
                        with open(task_file, "r+") as f:
                            for line in f:
                                listline = line.split(",")
                                list_of_tasks.append(listline) 
                        for i in range(0, len(list_of_tasks)):
                            if list_of_tasks[i][1] == users_task:
                                if list_of_tasks[i][5] == " No":
                                    list_of_tasks[i][5] = " Yes"
                                else:
                                    if list_of_tasks[i][5] == " No\n":
                                        list_of_tasks[i][5] = " Yes\n"
                        # Change the list back to a comma separated string.
                        for task in list_of_tasks:
                            for category in task:
                                if category == task[5]:
                                    pass
                                else:
                                    category += ","
                                string_of_tasks += category
                        # Write the string to file.
                        with open(task_file, "w") as f:
                            f.write(string_of_tasks)


                    # If user chose 'e', allow user to select whether to change
                    # username of taskholder or change due date for task.
                    elif one_task_choice == "e":
                        # Change txt file data into a list of sublists with no commas.
                        with open(task_file, "r+") as f:
                            for line in f:
                                listline = line.split(",")
                                list_of_tasks.append(listline)
                        # Find the sublist that matches the selected task and check if
                        # it is complete or not. If not, allow user to change the date or
                        # the username of the taskholder. If so, inform user that
                        # task is complete thus cannot be edited.
                        for i in range(0, len(list_of_tasks)):
                            if list_of_tasks[i][1] == users_task:
                                if list_of_tasks[i][5] == " No\n" or list_of_tasks[i][5] == " No":
                                    adjustment = input("Press 'u' to change user or 'd' to change date: ")
                                    if adjustment == "u":
                                        new_user = input("Enter the new username: ")
                                        list_of_tasks[i][0] = new_user
                                    else:
                                        if adjustment == "d":
                                            date = list_of_tasks[i][4]
                                            new_date = input("Enter the new due date: ")
                                            new_date = new_date[:0] + " " + new_date[0:]
                                            list_of_tasks[i][4] = new_date
                                else:
                                    print("Sorry this task can't be edited because it has been marked as complete.")
                        # Put the commas back into the lists and then
                        # change the lists into one long string
                        for task in list_of_tasks:
                            for category in task:
                                if category == task[5]:
                                    pass
                                else:
                                    category += ","
                                string_of_tasks += category
                        # Write the new string back to the file
                        with open(task_file, "w") as f:
                            f.write(string_of_tasks)
                            

                    # If user chose 'b', let them go back to all their tasks.      
                    else:
                        if one_task_choice == "b":
                            one_task = False
                            

            # If user chose -1, let them go back to main menu.               
            elif choice == -1:
                task_chooser = False
                running = False

            # If user did not make a valid choice, inform them.    
            else:
                print("\nThat was not a valid entry: ")


def view_stats():
    """This function looks inside task_overview.txt and user_overview.txt
    and prints the insights from those two files to the screen in a
    user friendly manner.
    """
    # Look in task_overview.txt and print contents to screen in a formatted string.
    with open("task_overview.txt", "r") as f:
        for line in f:
            listline = line.split(", ")
        print(f'''\nTask Overview:

{listline[0]}: {listline[1]}
{listline[2]}: {listline[3]}
{listline[4]}: {listline[5]}
{listline[6]}: {listline[7]}
{listline[8]}: {listline[9]}
{listline[10]}: {listline[11]}
''')

        
    # Look in user_overview.txt and print contents to screen in a formatted string.
    user_overview_string = "User Overview:\n\n"
    with open("user_overview.txt", "r") as f:
        for line in f:
            listline = line.split(", ")
            user_overview_string += f'''{listline[0]}
Total number of tasks assigned to user:                     {listline[2]}      
Percentage of total number of tasks assigned to user:       {listline[4]}
Percentage of tasks assigned to user that are complete:     {listline[6]}
Percentage of tasks assigned to user to still be completed: {listline[8]}
Percentage of tasks assigned to user that are overdue:      {listline[10]}\n'''
    print(user_overview_string)


def generate_reports():
    """This function generates two files, task_overview.txt and
    user_overview.txt and fills them with data insights gleaned from
    user.txt and tasks.txt.
    """
    # Declare variables to store data about tasks
    list_of_tasks = []
    dict_of_tasks = {}
    uncompleted_tasks = 0
    completed_tasks = 0
    overdue_tasks = 0
    percent_incomplete = 0
    percent_overdue = 0

    
    # Look at each task in task file.
    with open("tasks.txt", "r+") as f:
        for line in f:
            listline = line.split(",")
            # Check if task is incomplete.
            if listline[5] == " No\n" or listline[5] == " No":
                uncompleted_tasks += 1
                # Check if task is overdue.
                due_date = listline[4][1:]
                current_date = datetime.date(datetime.now())
                due_date = datetime.strptime(due_date, '%d %b %Y').date()
                if current_date > due_date:
                    overdue_tasks += 1  
            # Check if task is complete.
            else:
                if listline[5] == " Yes\n":
                    completed_tasks += 1
            list_of_tasks.append(listline)
            # Work out percentages for complete and incomplete tasks.
            percent_incomplete = (uncompleted_tasks / len(list_of_tasks)) * 100
            percent_overdue = (overdue_tasks / len(list_of_tasks)) * 100

            
        # Build a dictionary to store data about tasks.
        dict_of_tasks["Total tasks"] = len(list_of_tasks)
        dict_of_tasks["Completed tasks"] = completed_tasks
        dict_of_tasks["Uncompleted tasks"] = uncompleted_tasks
        dict_of_tasks["Overdue tasks"] = overdue_tasks
        dict_of_tasks["Percent incomplete"] = round(percent_incomplete, 2)
        dict_of_tasks["Percent overdue"] = round(percent_overdue, 2)

        
    # Write data to task_overview file.
    with open("task_overview.txt", "w") as f:
        f.write(f'''Total tasks, {dict_of_tasks["Total tasks"]}, Completed tasks, {dict_of_tasks["Completed tasks"]}, Uncompleted tasks, {dict_of_tasks["Uncompleted tasks"]}, Overdue tasks, {dict_of_tasks["Overdue tasks"]}, Percent incomplete, {dict_of_tasks["Percent incomplete"]}, Percent overdue, {dict_of_tasks["Percent overdue"]}''')


    # Declare variables to store data about users.
    users_and_passwords = []
    list_of_users = []
    users_and_tasks = {}
    task = 0
    users_incomplete_tasks = 0
    users_complete_tasks = 0
    users_overdue_tasks = 0
    user_overview_string = ""

    
    # Look in user file and build a list of users.
    with open("user.txt", "r") as f:
        for line in f:
            listline = line.split(",")
            users_and_passwords.append(listline[0])
    for user in users_and_passwords:
        list_of_users.append(user)

        
    # Look in list of tasks for tasks that correspond to users.
    for i in range(0, len(list_of_users)):
        for n in range(0, len(list_of_tasks)):
            # If you find that user in the task list...
            if list_of_users[i] == list_of_tasks[n][0]:
                # Get the due date for their task.
                users_due_date = list_of_tasks[n][4][1:]
                users_due_date = datetime.strptime(users_due_date, '%d %b %Y').date()
                # Count the tasks given to this user so far.
                task += 1
                # If the task is complete, count it as a completed task.
                if list_of_tasks[n][5] == " Yes\n" or list_of_tasks[n][5] == " Yes":
                    users_complete_tasks += 1
                # If the task is not complete, count it as an incomplete task.
                elif list_of_tasks[n][5] == " No\n" or list_of_tasks[n][5] == " No":
                        users_incomplete_tasks += 1
                        # If the task is overdue, count it as an overdue task.
                        if users_due_date < current_date:
                            users_overdue_tasks += 1

                            
        # Work out percentages for complete, incomplete and overdue tasks. 
        percentage = round((task / len(list_of_tasks)) * 100, 2)
        if task > 0:
            percent_complete = round((users_complete_tasks / task) * 100, 2)
            percent_incomplete = round((users_incomplete_tasks / task) * 100, 2)
            percent_overdue = round((users_overdue_tasks / task) * 100, 2)
        else:
            percent_complete = 0
            percent_incomplete = 0
            percent_overdue = 0

            
        # Build everything into a formatted string.
        user_overview_string += f'''{list_of_users[i]}, Total tasks assigned, {task}, Percent of tasks assigned, {percentage}, Percent complete, {percent_complete}, Percent remaining, {percent_incomplete}, Percent overdue, {percent_overdue}\n'''
        users_and_tasks[list_of_users[i]] = task
        task = 0
        users_complete_tasks = 0
        users_incomplete_tasks = 0
        users_overdue_tasks = 0

        
    # Write the formatted string to file.
    with open("user_overview.txt", "w") as f:
        f.write(user_overview_string)

    
#****************************************************************
#****************************LOG IN******************************

# Set up boolean variables to handle login process

logged_in = False
got_username = False
got_password = False


# While not logged in...
while logged_in == False:
    # If the program has not been given a valid username yet, ask for one.
    if got_username == False:
        username = input("Enter your username: ")

        
        # Check if it matches any of the usernames in the file.
        with open("user.txt", "r") as f:
            for line in f:
                listline = line.split()
                file_username = listline[0].replace(",", "")

                
                # If we find a match on one of the lines...
                if username == file_username:
                    got_username = True

                    
                    # ask user for their password and see if it matches.
                    while got_password == False:
                        password = input("Please enter your password: ")
                        # If so, log them in
                        if password == listline[1]:
                            got_password = True
                            logged_in = True
                            print("You're logged in")
                        # If not, let user know their entry was invalid.
                        else:
                            print("Sorry, this password is invalid.")


            # If you get to the end of the loop and the username has still
            # not been found let the user know, and restart the process
            if got_username == False:
                print("Sorry, this username is invalid.")


#***********************************************************************
#**************************MANAGE TASKS*********************************
                
# If program gets to this stage, it means user is logged in.

# Set a 'running' boolean so that after the user requests an option
# and gets presented with their request,
# they get presented with the options menu again and can keep
# engaging with the app.


running = True
reports_generated = False


# Display different options for admin users versus other users.
while running:
    if username == "admin": 
        option = input('''\nPlease select one of the following options: 
        r - register user 
        a - add task 
        va - view all tasks 
        vm - view my tasks 
        ds - display statistics
        gr - generate reports
        e - exit ''')
    else:
        option = input('''\nPlease select one of the following options: 
        a - add task 
        va - view all tasks 
        vm - view my tasks 
        e - exit ''')


    # If admin user selected "r", allow them to add a new user. 
    if option == "r" and username == "admin":
        reg_user(user_file)


    # If admin user selected "ds", show them stats about the tasks. 
    elif option == "ds" and username == "admin":
        if reports_generated == False:
            generate_reports()
            reports_generated = True
            view_stats()
        else:
            view_stats()

        
    # If admin user selected "gr", generate reports about the tasks. 
    elif option == "gr" and username == "admin":
        generate_reports()

    # If user selected "a" allow them to add a task.
    
    elif option == "a":
        add_task(task_file)

    # If user selected "va", allow them to view all tasks.
    
    elif option == "va":
        view_all(task_file)


    # If user selected "vm", allow them to view their tasks.
    elif option == "vm":
        view_mine(task_file)


    # If user selected "e", exit the program.
    else:
        if option == "e":
            print("App closed")
            running = False


# Resources used:
# Researched how to append here: https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
# Date formatting found here: https://thispointer.com/python-how-to-convert-datetime-object-to-string-using-datetime-strftime/
# Researched how to append to end of file here: https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
