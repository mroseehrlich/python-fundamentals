###############################################################################
# Mia Ehrlich
# Lab 02
# This program introduces the Lame Game, displays a welcome message with a brief
# description of the game, prompts the user for their name, displays a menu
# with user options, and then returns a message to the user with their name and
# choice of menu options
###############################################################################


#Display welcome message
print('Welcome to the Lame Game!')
print('Are you feeling lame? Let\'s play and find out!')
print()

#Get user name
name = input('What is your name? ')
print()

#Display menu and prompt for user input
print('MENU')
print('1. Make Change')
print('2. High Card')
print('3. Quit')
print()
menu_option = int(input('Enter the number of your menu option: '))
print()

#Displey message to user with name and menu option
print('Hello', name, ', you chose menu option', str(menu_option), '.')
