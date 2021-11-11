#!/usr/bin/env python3

import sys
from menu import Menu

menu = Menu()
args = sys.argv

try:
    arg = args[1]

    if(arg == 'help'):
        menu.help()
    elif(arg == 'add_task'):
        menu.add_task()
    else:
        print('Wrong argument! Please try to use "help"')
except:
    menu.welcome_message()
