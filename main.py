#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from countdown import count_regressive, count_bye
from clear import clear_screen
from query import path_indicator

# SPREADSHEET PATH INDICATOR

def indicator():
    print('\t\n *** THIS PROGRAM IS A CONSTRUCTOR OF PARTNERS DATA ***\n')
    print('\t\n === USE THIS FOR POPULATE THE dbfornecedores on site ===\n')
    option = input('\t\n Choose your OS below:\t\n - Type:\t\n\n'+
                   '"1" for *NIX\t\n"2" for WIN\t\n"0" for EXIT\t\n\n\n->')
    if option == '1':
        clear_screen()
        path = input('\t\nInsert the path...\t\nEx:\n'+
                        '/home/<user>/Documents/<spreadsheat.*>"\t\n\n'+
                        '->')
        path_indicator(path)
        #clear_screen()
    elif option == '2':
        clear_screen()
        path = input('\t\nInsert the path...\t\nEx:\n'+
                        'C:\\Users\\<user>\\Documents\\<spreadsheat.*>"\t\n\n'+
                        '->')
        path_indicator(path)
        clear_screen()
    elif option == '0':
        clear_screen()
        count_bye()
    else:
        clear_screen()
        count_regressive()
        clear_screen()
        indicator()
        option = ''  

# MAIN CALL

if __name__ == '__main__':
    while True:
        indicator()