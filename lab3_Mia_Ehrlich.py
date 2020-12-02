###############################################################################
# Mia Ehrlich
# Lab 04
# This program introduces the Lame Game, displays a welcome message with a brief
# description of the game and an option menu for gaming rooms.
# If user chooses menu option 1, they play the make change game, which prompts user
# for the cost of an item, the amout paid, confirms that the amout paid is more
# than the cost, then calculates change back in dollars, quarters, nickels,
# dimes, and pennies.
# If user chooses menu option 2, the program prints a message to user
# If user enters option 3, their input is not accounted for by the decision
# structure, and the program ends
# If user chooses a number less than one or greater than 3, the program prints
# a message to user that their menu option is not valid
###############################################################################


#Display welcome message
print('Welcome to the Lame Game!')
print('Are you feeling lame? Let\'s play and find out!')


#Display menu and prompt for user input
print('\nMENU')
print('1. Make Change')
print('2. High Card')
print('3. Quit\n')
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
    
elif menu_option == 2:
    print('High Card is coming soon.')
elif menu_option < 1 or menu_option > 3:
    print('Invalid option') 
