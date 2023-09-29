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

def total(shopping_list=shopping_list):
    total_price = 0
    for k, v in shopping_list.items():
        total_price += (v[0] * v[1])
    print(f'Total: ${round(total_price, 2)}')


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
                break # Break the loop if conversion to int is successful
            except ValueError:
                print('Please only enter a whole number.')
    if product in shopping_list:
        shopping_list[product][1] += quantity # No need to add a new key, just update the quantity 
    else:
        shopping_list[product] = [price, quantity] # A new key:value pair is set up if it doesn't already exist
    print(f'\nYou have added {quantity} {product} to your cart.\n')
    print('Items in Cart:')
    for k, v in shopping_list.items():
        print(f'\t{v[1]} {k} ${round(v[0] * v[1], 2)}')
    total(shopping_list)


def remove_from_cart():
    item_to_remove = input('What would you like to remove from your cart?\n\t').title()
    if item_to_remove not in shopping_list:
        print("\nThat item is not in your cart.")
    elif item_to_remove in shopping_list and shopping_list[item_to_remove][1] == 1:
            del shopping_list[item_to_remove]
            print(f'{item_to_remove} has been removed from your cart.\n')
            print('Items in Cart:')
            for k, v in shopping_list.items():
                print(f'\t{v[1]} {k} ${round(v[0] * v[1], 2)}')
            return total(shopping_list)
    else:
        while True:
            quantity_to_remove_input = input(f'How many {item_to_remove} would you like to remove?\n\t')
            try:
                quantity_to_remove = int(quantity_to_remove_input)
                break # Break the loop if conversion to int is successful
            except ValueError:
                print('Please only enter a whole number.')
    for k, v in shopping_list.items():
        if k == item_to_remove:
            shopping_list[k][1] -= quantity_to_remove
            print(f'\n{quantity_to_remove} {item_to_remove} have been removed from your cart.\n')
    if shopping_list[item_to_remove][1] == 0:
        del shopping_list[item_to_remove]
    print('Items in Cart:')
    for k, v in shopping_list.items():
        print(f'\t{v[1]} {k} ${round(v[0] * v[1], 2)}')
    total(shopping_list)






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


# shopping_cart_1 = {'Apples': [2.99, 4], 'Bananas': [1.99, 3]}
# new_quantity = 0
# quantity_to_remove = 3

# for k, v in shopping_cart_1.items():
#     shopping_cart_1[k][1] -= quantity_to_remove 

# print(shopping_cart_1)

