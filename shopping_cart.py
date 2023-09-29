# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.


import os
def clear_output():
    os.system('cls')

shopping_list = {}
total_price = 0

def total(shopping_list):
    total_price = 0
    for k, v in shopping_list.items():
        total_price += (v[0] * v[1])
    print(f'Total: {total_price}')


def add_to_cart():
    product = input('What would you like to add to your cart?\n\t').title()
    if product in shopping_list:
        while True:
            quantity_input = input('How much of this product would you like to add?\n\t')
            try:
                quantity = int(quantity_input)
                break # Break the loop if conversion to float is successful
            except ValueError:
                print('Please only enter a whole number.')
    else:
        while True:
            price_input = input('How much does this item cost?\n\t')
            try:
                price = float(price_input)
                break # Break the loop if conversion to float is successful
            except ValueError:
                print('Please only enter a number.')
        while True:
            quantity_input = input('How much of this product would you like to add?\n\t')
            try:
                quantity = int(quantity_input)
                break # Break the loop if conversion to float is successful
            except ValueError:
                print('Please only enter a whole number.')

    if product in shopping_list:
        shopping_list[product][1] += quantity
    else:
        shopping_list[product] = [price, quantity]
    print(f'Success! You have added {quantity} {product} to your cart.')
    print('Items in Cart:')
    for k, v in shopping_list.items():
        print(f'\t{v[1]} {k} {v[0] * v[1]}')
    total(shopping_list)

def remove_from_cart():
    item_to_remove = input('What would you like to remove from your cart?\n')





def shopping_cart():
    active = True
    potential_responses = {'add', 'remove', 'clear', 'quit'}
    while active:
        initial = input('What would you like to do?\n(Add / Remove / Clear / Quit)\t').lower()
        if initial == 'quit':
            active = False
        elif initial not in potential_responses: 
            print('Sorry, but that is not a valid response.')
        elif initial == 'add':
            add_to_cart()
        elif initial == 'remove':
            remove_from_cart() 
        elif initial == 'clear':
        # clear_from_cart() function
            print('Your cart has been cleared!')







shopping_cart()
