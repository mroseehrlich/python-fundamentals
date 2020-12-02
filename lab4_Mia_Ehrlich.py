#######################################################################################
# Mia Ehrlich
# Lab 04
# This program introduces the Lame Game, displays a welcome message with a brief
# description of the game and an option menu for gaming rooms. The menu options
# use an input validation loop to ensure the user picks only options 1, 2, or 3.
# If user chooses menu option 1, they play the make change game, which prompts the user
# for the cost of an item, the amout paid, confirms that the amout paid is more
# than the cost, then calculates change back in dollars, quarters, nickels,
# dimes, and pennies.
# If user chooses menu option 2, they play the high card game which asks for the
# names of two players, asigns a random card to be drawn for each player, then
# displays each card drawn and the winner with the higher card. 
# The gaming option menu displays again after one round of either game.
# If user enters option 3, the program ends.
#######################################################################################

#Import code for randint function
import random

#Display welcome message
print('Welcome to the Lame Game!')
print('Are you feeling lame? Let\'s play and find out!')

#Display menu and prompt for user input
print('\nMENU')
print('1. Make Change')
print('2. High Card')
print('3. Quit\n')
menu_option = int(input('Enter the number of your menu option: '))

#Set a condition loop for menu to display until player wants to quit
while menu_option != 3:

    #Menu option input validation
    while menu_option < 1 or menu_option > 3:
        print('Invalid option.')
        menu_option = int(input('Enter the number of your menu option: '))
    
    # Decision structure based on menu option

    if menu_option == 1:
    
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
            
    #High Card game if gamer chooses menu option 2
    elif menu_option == 2:

        #Get players' names
        player1 = input('\nWhat is your name, Player 1? ')
        player2 = input('What is your name, Player 2? ')
        print()

        
        #Set card 1 and 2 to random ints between 1 and 13 to deal cards
        card1 = random.randint(1, 13)
        card2 = random.randint(1, 13)

        #Decision structure for displaying card 1's value
        #Display the name of player one and the value of their card
        if card1 == 1:
            print(player1, 'drew an ace.')
        elif card1 == 2:
            print(player1, 'drew a 2.')
        elif card1 == 3:
            print(player1, 'drew a 3.')
        elif card1 == 4:
            print(player1, 'drew a 4.')
        elif card1 == 5:
            print(player1, 'drew a 5.')
        elif card1 == 6:
            print(player1, 'drew a 6.')
        elif card1 == 7:
            print(player1, 'drew a 7.')
        elif card1 == 8:
            print(player1, 'drew a 8.')
        elif card1 == 9:
            print(player1, 'drew a 9.')
        elif card1 == 10:
            print(player1, 'drew a 10.')
        elif card1 == 11:
            print(player1, 'drew a jack.')
        elif card1 == 12:
            print(player1, 'drew a queen.')
        elif card1 == 13:
            print(player1, 'drew a king.')

        #Decision structre for displaying card 2
        #Display the name of player two and the value of their card
        if card2 == 1:
            print(player2, 'drew an ace.')
        elif card2 == 2:
            print(player2, 'drew a 2.')
        elif card2 == 3:
            print(player2, 'drew a 3.')
        elif card2 == 4:
            print(player1, 'drew a 4.')
        elif card2 == 5:
            print(player2, 'drew a 5.')
        elif card2 == 6:
            print(player2, 'drew a 6.')
        elif card2 == 7:
            print(player2, 'drew a 7.')
        elif card2 == 8:
            print(player2, 'drew a 8.')
        elif card2 == 9:
            print(player2, 'drew a 9.')
        elif card2 == 10:
            print(player2, 'drew a 10.')
        elif card2 == 11:
            print(player2, 'drew a jack.')
        elif card2 == 12:
            print(player2, 'drew a queen.')
        elif card2 == 13:
            print(player2, 'drew a king.')
            
        #Compare which card is higher then print the winning player
        if card1 > card2:
            print(player1, 'wins!!!')
        else:
            print(player2, 'wins!!!')
        

    #Display game menu and get input for another game menu option
    print()
    print('Would you like to play another game?')
    print('\nMENU')
    print('1. Make Change')
    print('2. High Card')
    print('3. Quit\n')
    menu_option= int(input('Enter the number of your menu option: '))
    
