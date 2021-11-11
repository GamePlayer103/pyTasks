from datetime import datetime

class Task():
    """Single task"""
    
    def __init__(self, title, description='none', end_date='none'):
        self.title = title
        self.description = description
        current_date = datetime.now().strftime('%d/%m/%y')
        self.create_date = current_date 
        self.end_date = end_date

    def get_info(self):
        """Return informations about the task"""
        info = (f'Title: {self.title}\n'
                f'Description: {self.description}\n'
                f'Create date: {self.create_date}\n'
                f'End date: {self.end_date}\n')
        return info
