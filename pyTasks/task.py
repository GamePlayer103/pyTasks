from datetime import datetime
import json

class Task():
    """Single task"""
    
    def __init__(self, title, description='', end_date=''):
        self.title = title

        if(description != ''):
            self.description = description
        else:
            self.description = 'none'

        current_date = datetime.now().strftime('%d/%m/%y')
        self.create_date = current_date

        if(self.validate_date_format(end_date) == True):
            self.end_date = end_date
        else:
            self.end_date = 'none'

    @staticmethod
    def validate_date_format(date_str):
        """Validate date format from string""" 
        try:
            datetime_obj = datetime.strptime(date_str, '%d/%m/%y').strftime('%d/%m/%y')
            return True
        except: 
            return False

    def get_info(self):
        """Return informations about the task"""
        info = (f'Title: {self.title}\n'
                f'Description: {self.description}\n'
                f'Create date: {self.create_date}\n'
                f'End date: {self.end_date}\n')
        return info

    def save_to_file(self):
        """Save task to JSON file"""
        task_dict = {'title': self.title,
                'description': self.description,
                'end_date': self.end_date,
                'create_date': self.create_date}

        with open('tasks.json', 'r+') as file:
            data = json.load(file)
            data.append(task_dict)
            file.seek(0)
            json.dump(data, file)
