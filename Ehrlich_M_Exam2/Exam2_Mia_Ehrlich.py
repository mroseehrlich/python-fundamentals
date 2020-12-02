

#Name: Mia Ehrlich
def return_value(item_qty, item_price):
    value = format(item_qty * item_price, '.2f')
    return value

def main():

    try:
    
        print('Name\tQuantity\tPrice\tValue')
        
        inventory_file = open("Exam2.txt", 'r')

        name = inventory_file.readline()

        while name != '':
            qty = int(inventory_file.readline())
            price = float(inventory_file.readline())

            name = name.rstrip('\n')

            value = return_value(qty, price)


            print(name, '\t', qty, '\t', price, '\t', value)

            name = inventory_file.readline()
        
        inventory_file.close()

    except IOError as err:
        print('Error: ' + err)

    except Exception as err:
        print ('Error: ' + err)
        

main()
            
