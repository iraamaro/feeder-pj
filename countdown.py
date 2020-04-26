# -*- coding: utf-8 -*-

#  COUNTDOWN MODULE

import time
import sys
from clear import clear_screen


def count_bye():
    print('\t\n\nGOODBYE\n\n')
    print('\t\nShutdown in 3 seconds...\n\n')
    t = 3
    while t >= 1:
        print(t, '\n')
        time.sleep(1)
        t -= 1
    clear_screen()
    sys.exit()
    sys.exit()
        
def count_regressive():
    print('\t\n\nWRONG OPTION\n\n')
    print('\t\nChoose again... in 5 seconds...\n\n')
    t = 5
    while t >= 1:
        print(t, '\n')
        time.sleep(1)
        t -= 1
    clear_screen()

def feed(n):
    if len(n) % 3 == 0:
        cheat()
        
def cheat():
    t = 90
    while t >= 1:
        print(t, '\n')
        time.sleep(1)
        t -= 1
    clear_screen()
        
def cheat_hard():
    clear_screen()
    print("\t\nHARD CHEAT ENABLED.\t\nWaiting 180s. Maybe time for a coffee?")
    t = 180
    while t >= 1:
        time.sleep(1)
        t -= 1
    clear_screen()