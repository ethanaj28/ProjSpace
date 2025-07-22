import sys
import time

print('*' * 50)
print('Welcome to Budget Calculator')
print('Chose duration type: ')
#print('Chose duration type (or type "help"): ')
print('y = year(s) m = month(s) w = week(s) ')
print('*' * 50)


a = ''
b = ''
char = 'abcdefghijklmnopqrstuvwxyz!@#%^&*()_+$,<>/?;[]{}"|'
mytable = str.maketrans(a, b, char)


while True:
    dur = input('Enter duration type: ').lower()
    total = input('How much is the total purchase? ')
    totalf = float(total.translate(mytable))

    if dur == 'y':
        lengy = float(input('You chose to budget by year(s), how many? '))
        yearcomf = input(f'You are looking to budget ${totalf:.2f} by {lengy} year(s), correct? ').lower()
        if yearcomf == 'y':
            yeartotal = totalf / lengy
            print(f'\n${yeartotal:.2f} /year\n')
            time.sleep(6)
            sys.exit(0)
        else:
            print('\nPlease make the appropriate corrections.\n')

    elif dur == 'm':
        lengm = float(input('You chose to budget by month(s), how many? '))
        monthcomf = input(f'You are looking to budget ${totalf:.2f} by {lengm} month(s), correct? ').lower()
        if monthcomf == 'y':
            monthtotal = totalf / lengm
            print(f'\n${monthtotal:.2f} /month\n')
            time.sleep(6)
            sys.exit(0)
        else:
            print('\nPlease make the appropriate corrections.\n')

    elif dur == 'w':
        lengw = float(input('You chose to budget by week(s), how many? '))
        weekcomf = input(f'You are looking to budget ${totalf:.2f} by {lengw} week(s), correct? ').lower()
        if weekcomf == 'y':
            weektotal = totalf / lengw
            print(f'\n${weektotal:.2f} /week\n')
            time.sleep(6)
            sys.exit(0)
        else:
            print('\nPlease make the appropriate corrections.\n')

    else:
        print('\nPlease select the correct budget type.\n')