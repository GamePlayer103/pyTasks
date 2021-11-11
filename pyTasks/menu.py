import getpass
from task import Task

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
        print('New task added succesfully!')
