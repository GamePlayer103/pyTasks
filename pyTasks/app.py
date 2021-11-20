#!/usr/bin/env python3

import sys
from menu import Menu

menu = Menu()
args = sys.argv

try:
    arg = args[1]
except:
    menu.welcome_message()
    exit()

if(arg == 'help'):
    menu.help()
elif(arg == 'add_task'):
    menu.add_task()
elif(arg == 'tasks'):
    menu.display_tasks()
else:
    print('Wrong argument! Please try to use "help"')
