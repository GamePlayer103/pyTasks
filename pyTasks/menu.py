import getpass

class Menu():
    """Displays simple text menu, allowing user to manage tasks"""

    def get_welcome_message(self):
        """Returns simple welcome message"""
        username = getpass.getuser()
        msg = ('=== pyTasks ===\n'
                f'Welcome, {username}\n')
        return msg 
