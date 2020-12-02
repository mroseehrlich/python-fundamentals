#######################################################################################
# Mia Ehrlich
# Lab 06
# This program introduces the Lame Game, displays a welcome message with a brief
# description of the game and an option menu for gaming rooms. Input validation
# ensures that the user picks only options 1, 2, 3, or 4 from the menu list.
# If user chooses menu option 1, they play the Make Change game, which prompts the user
# for the cost of an item, the amout paid, confirms that the amout paid is more
# than the cost, then calculates change back in dollars, quarters, nickels,
# dimes, and pennies.
# If user chooses menu option 2, they play the High Card game which asks for the
# names of two players, asigns a random card to be drawn for each player, then
# displays each card drawn and the winner with the higher card. 
# The gaming option menu displays again after one round of either game.
# If user chooses option 3, they play the Deal Hand game, which deals five cards and
# displays their respective values.
# If user chooses option 4, they play Save Dream Hand, which prompts them for
# card values between 1 and 13 and saves their cards to a file.
# If the user chooses option 5, the play Display Dream Hand, which reads their
# five card hand from Save Dream Hand and displays the face value of each card.
# If user chooses option 6, the game ends.
# All code is organized into functions called by the main driver function
#######################################################################################

# Import code for randint function
import random

# Function: main()
# Inputs: none
# Outputs: none
# The main() function prints a welcome message to the Lame Game, displays an
# option menu for gaming rooms, then calls the functions that allow the user to play
# access a game depending on their menu option choice
def main():
    #Display welcome message
    print('Welcome to the Lame Game!')
    print('Are you feeling lame? Let\'s play and find out!')

    #Display menu
    menu_option = display_menu()

    #Set a condition loop for menu to display until player wants to quit
    while menu_option != 6:
        # Decision structure based on menu option 
        if menu_option == 1:
            make_change()
        elif menu_option == 2:
            high_card()
        elif menu_option == 3:
            deal_hand()
        elif menu_option == 4:
            save_dream_hand()
        elif menu_option == 5:
            display_dream_hand()
        #repeat menu display until user selects quit
        menu_option = display_menu()

# Function: display_menu()
# Inputs: none
# Outputs: menu_option
# Purpose: the display_menu() function displays a manu with three options for gaming rooms
# and a fourth option for quit, prompts the user for input, validates input with
# a validation loop, then return the menu_optionThis function blah blah blah…..
def display_menu():
    # Display menu and prompt for user input
    print('\nMENU')
    print('1. Make Change')
    print('2. High Card')
    print('3. Deal Hand')
    print('4. Save Dream Hand')
    print('5. Display Dream Hand')
    print('6. Quit\n')

    menu_option = int(input('Enter the number of your menu option: '))
    while menu_option < 1 or menu_option > 6:
        print('Invalid option.')
        menu_option = int(input('Enter the number of your menu option: '))

    return menu_option

# Function: make_change()
# Inputs: none
# Outputs: none
# Purpose: the make_change() function prompts the user for input for the cost of an item
# and the amout paid, then displays the change in dollars, quarters, dimes,
# nickels, and pennies
def make_change():
    print('\nMAKE CHANGE\n')
        
    # Get input for cost of item and amount paid
    amount_owed = float(input('Amount owed: '))
    amount_paid = float(input('Amount paid: '))

    if amount_owed > amount_paid:
        print('\nI\'m sorry. That is not enough money to cover the cost of the item.')
    else:    
        #Calculate and display change due
        change = amount_paid - amount_owed
        print('\nChange back: $', format(change, '.2f'), sep='')

        # Calculate and display dollars back as int
        # Update change back amount as int
        # Add 0.001 to amount to address rounding error caused by
        # Conversion of float to int to prevent loss of penny amount
        # Multiply by 100 to use change amount as an integer
        dollars = int(change // 1)
        change = int(((change - dollars) + .001) * 100)
        
        # Calculate quarters back
        #And update new change variable
        quarters = change // 25
        change = change - (quarters * 25)

        # Calculate dimes back
        # And update new change variable
        dimes = change // 10
        change = change - (dimes * 10)

        # Calculate nickels back
        # And update new change variable
        nickels = change // 5
        change = change - (nickels * 5)

        # Calculate pennies back
        pennies = change

        # Print change back in coins amounts
        #If coin amounts = 1, print singular coin
        #Else print plural coins
        print('\nYour change is:\n')
        if dollars == 1:
            print(dollars, 'dollar')
        else:
            print(dollars, 'dollars')
            
        if quarters == 1:
            print(quarters, 'quarter')
        else:
            print(quarters, 'quarters')
            
        if dimes == 1:
            print(dimes, 'dime')
        else:
            print(dimes, 'dimes')

        if nickels == 1:
            print(nickels, 'nickel')
        else:
            print(nickels, 'nickels')

        if pennies == 1:
            print(pennies, 'penny')
        else:
            print(pennies, 'pennies')

# Function: display_face_value()
# Inputs: cardValue
# Outputs: none
# Purpose: the display_face_value() function passes a number represented by the cardValue
# variable as a perameter and then uses a decision structure to set a secondary
# variable associated with that number for a display card valueas Ace, 1-10,
# Jack, Queen, or , then returns the display card value
def display_face_value(card_value):
    display_card = ""
    if card_value == 1:
        display_card = 'Ace'
    elif card_value == 2:
        display_card = 'Two'
    elif card_value == 3:
        display_card = 'Three'
    elif card_value == 4:
        display_card = 'Four'
    elif card_value == 5:
        display_card = 'Five'
    elif card_value == 6:
        display_card = 'Six'
    elif card_value == 7:
        display_card = 'Seven'
    elif card_value == 8:
        display_card = 'Eight'
    elif card_value == 9:
        display_card = 'Nine'
    elif card_value == 10:
        display_card = 'Ten'
    elif card_value == 11:
        display_card = 'Jack'
    elif card_value == 12:
        display_card = 'Queen'
    elif card_value == 13:
        display_card = 'King'
    print(display_card)

# Function: high_card()
# Inputs: none
# Outputs: none
# Purpose: the high_card() function takes user input for the names of two players, sets
# one card for each player as a random number between 1 and 13, displays the
# name of the player and the face value of their card using the display_face_value()
#function, compares which card is higher, and displays the winner with the highest card
def high_card():
    #Display the High Card game name
    print('\nHIGH CARD\n')
    
    # Get players' names
    player1 = input('\nWhat is your name, Player 1? ')
    player2 = input('What is your name, Player 2? ')
    print()

        
    # Set card 1 and 2 to random ints between 1 and 13 to deal cards
    card1 = random.randint(1, 13)
    card2 = random.randint(1, 13)

    # Decision structure for displaying card 1's value
    # Display the name of player one and the value of their card
    print(player1, 'drew a ', end='')
    display_face_value(card1)

    # Decision structre for displaying card 2
    # Display the name of player two and the value of their card
    print(player2, 'drew a ', end='')
    display_face_value(card2)
        
    # Compare which card is higher then print the winning player
    if card1 > card2:
        print(player1, 'wins!!!')
    elif card2 > card1:
        print(player2, 'wins!!!')
    else:
        print(player1, 'and', player2, 'tie!!!')

# Function: deal_hand()
# Inputs: none
# Outputs: none
# The deal_hand() function sets the value of 5 cards as a random integer between
# 1 and 13 and displays the face value of each card by calling display_face_value()
def deal_hand():
    # Introduce deal hand game
    print('\nDEAL HAND')
    print('\nLet\'s deal you a five card hand.')
    print('Here\'s what you drew:\n')

    # Create 5 variables to represent 5 cards and assign random integers
    # Between 1 and 13
    card1 = random.randint(1, 13)
    card2 = random.randint(1, 13)
    card3 = random.randint(1, 13)
    card4 = random.randint(1, 13)
    card5 = random.randint(1, 13)

    # Display the face cards by passing card variable into the display_face_card
    # function for each of the five cards
    display_face_value(card1)
    display_face_value(card2)
    display_face_value(card3)
    display_face_value(card4)
    display_face_value(card5)

# Function: save_dream_hand()
# Inputs: none
# Outputs: none
# Purpose: The save_dream_hand() function prompts the user for five cards with
# numbers between 1-13, validates the input, then prompt the user to enter a file
# name, and writes the five cards to the file, alerting the user that the file
# was saved. If a value error is raised due to the user entering a non-integer
# value, an except suit runs to notify the user of their error.
def save_dream_hand():
    # Introduce save dream hand to user
    print('\nSAVE DREAM HAND\n')
    print('Please enter 5 cards by their associated numerical value.')
    print('Enter 1 for Ace, 2 through 10 for two through ten, and 11, 12, or 13 for face cards.\n')

    # Use try statement for default code that runs unless
    # Python interpreter encounters an error
    try:
        # Ask user for 5 dream cards with numbers between 1 and 13
        # And validate user input for each of the 5 cards
        save_card1 = int(input('Please enter a number for your first card: '))
        while save_card1 < 1 or save_card1 > 13:
            print('Invalid option.')
            save_card1 = int(input('Please enter a number for your first card: '))

        save_card2 = int(input('Please enter a number for your second card: '))
        while save_card2 < 1 or save_card2 > 13:
            print('Invalid option.')
            save_card2 = int(input('Please enter a number for your second card: '))

        save_card3 = int(input('Please enter a number for your third card: '))
        while save_card3 < 1 or save_card3 > 13:
            print('Invalid option.')
            save_card3 = int(input('Please enter a number for your third card: '))

        save_card4 = int(input('Please enter a number for your fourth card: '))
        while save_card4 < 1 or save_card4 > 13:
            print('Invalid option.')
            save_card4 = int(input('Please enter a number for your fourth card: '))

        save_card5 = int(input('Please enter a number for your fifth card: '))
        while save_card5 < 1 or save_card5 > 13:
            print('Invalid option.')
            save_card5 = int(input('Please enter a number for your fifth card: '))      

        # Prompt user to enter a file name to write cards to
        print('\nLet\'s save those cards to a file!')
        file_name = input('Please enter a file name: ')

    
        # Open infile in write mode
        dream_card_file = open(file_name, 'w')

        # Write each dream card number as a string to separate lines in file
        dream_card_file.write(str(save_card1) + '\n')
        dream_card_file.write(str(save_card2) + '\n')
        dream_card_file.write(str(save_card3) + '\n')
        dream_card_file.write(str(save_card4) + '\n')
        dream_card_file.write(str(save_card5) + '\n')

        #Close file and display to user that dream hand was saved to file
        dream_card_file.close()
        print('Your dream hand has been saved.')
        
    # Except suite displays error message if python interpreter encounters
    # a ValueError due to user inputting a string
    except ValueError:
        print('ERROR: Dream cards must be valid numbers!')
        
# Function: display_dream_hand()
# Inputs: none
# Outputs: none
# Purpose: The display_dream_hand() introduces the display dream hand gaming
# room, prompts the user for an existing file name, open the file, saves
# each line to a separate card variable, closes the file, and displays
# the face value of each card. If the user enters a file that is not recognized,
# an IOError exception is raised and the program displays an error message to
# the user.
def display_dream_hand():
    # Introduce Display Dream Hand
    print('\nDISPLAY DREAM HAND\n')
    print('\nDid you already save your dream hand? Enter an existing'+
          'file to see your hand!')
    
    # Prompt user for file name where dream hand was saved
    file_name = input('Please enter a file name: ')

    # Try suit runs default code
    try:
        # Open the file given by user input in read mode 
        infile = open(file_name, 'r')

        # Save each line of file to a card variable
        card1 = int(infile.readline())
        card2 = int(infile.readline())
        card3 = int(infile.readline())
        card4 = int(infile.readline())
        card5 = int(infile.readline())

        # Close file
        infile.close()
        
        # Display face value for each card
        display_face_value(card1)
        display_face_value(card2)
        display_face_value(card3)
        display_face_value(card4)
        display_face_value(card5)

    # Exception  suite prints error if user input file is not found
    # and an IOError is raised
    except IOError:
        print('ERROR: Your file was not found')
            
#Call main() function
main()
