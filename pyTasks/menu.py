import getpass
from task import Task
import json

class Menu():
    """Displays simple text menu, allowing user to manage tasks"""

    def welcome_message(self):
        """Prints simple welcome message"""
        username = getpass.getuser()
        msg = ('=== pyTasks ===\n'
                f'Welcome, {username}\n')
        print(msg) 

    def add_task(self):
        """Adds new task"""
        print('--- Adding new task ---')

        title = input('Title: ')
        description = input('Description: ')
        end_date = input('End date (d/m/y): ') 

        while(Task.validate_date_format(end_date) == False):
            if(end_date != ''):
                end_date = input('Wrong date format! End date (d/m/y): ')
            else:
                break

        task = Task(title=title, description=description, end_date=end_date)
        task.save_to_file()

        print('New task added succesfully!')

    def help(self):
        """Prints help message"""
        msg = ('pyTasks - simple program for managing daily tasks\n\n'
                'Options:\n'
                'help - displays help menu (like this one)\n'
                'add_task - adds new task\n')
        print(msg)

    def get_tasks(self):
        """Returns list of tasks from file"""
        with open('tasks.json', 'r') as file:
           data = json.load(file)
        tasks = []
        for x in data:
            tasks.append(Task(x['title'], description=x['description'], end_date=x['end_date'], create_date=x['create_date']))
        return tasks 

    def display_tasks(self):
        """Prints tasks"""
        for i in self.get_tasks():
            print(i.get_info())
