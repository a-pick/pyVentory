import re

def letter_counter(word:str) -> dict:
    '''
    Takes a string as an input and prints how many times each letter appears in the word.
    Outputs a dictionary containing these values.
    '''
    occurences = {}; original_word = word; word = word.lower()
    # create the dictionary
    for i in range(len(word)):
        if word[i] in occurences:
            occurences[word[i]] += 1
        else:
            occurences[word[i]] = 1
    # print the occurences, in alphabetical order
    occurences = {key: value for key, value in sorted(occurences.items())}
    for j in range(len(occurences)):
        print(f"The letter {list(occurences.keys())[j]} is in the string {original_word} {list(occurences.values())[j]} time(s).")
    return occurences

def add_item(inventory:dict) -> None:
    '''
    Adds an item to the inventory dictionary.
    ''' 
    msg = "Enter the number of items: "
    while True:
        try:
            name = str(input("Enter the name of the item: ")).title()
            if name != "":
                break
        except:pass
    while True:
        try:
            if name not in inventory:
                price = input("Enter the price of this item (format: 21.67): ")
                if re.match("[0-9]+.\d\d$", price):
                    break
            else:
                price = list(dict(inventory[name]).values())[0]
                break
        except:pass
    while True:
        try:
            count = int(input(msg))
            break
        except:msg = "Enter the number of items (must be an integer): "

    if name in inventory:
        inventory.update({name:{'price':float(price), 'count':list(dict(inventory[name]).values())[1] + count}})
    else:
        inventory.update({name:{'price':float(price), 'count':count}})
    
    print(f"{count} {name}(s) have been added to inventory")

def remove_item(inventory:dict) -> None:
    '''
    Removes an item from the inventory dictionary.
    '''
    msg = "Enter the number of items: "
    query = input("Enter the name of the item: ").title()
    if query not in inventory:
        print(f"There are no {query}(s) in inventory")
    elif query in inventory:
        while True:
            try:
                count = int(input(msg))
                inventory.update({query:{'price':list(dict(inventory[query]).values())[0], 'count':list(dict(inventory[query]).values())[1] - count}})
                print(f"{count} {query}(s) have been removed from inventory")
                break
            except:msg = "Enter the number of items (must be an integer): "

def calc_worth(inventory:dict) -> None:
    total_value = 0.00
    sorted_inventory = {key: value for key, value in sorted(inventory.items())}
    for i in range(len(sorted_inventory)):
        values = list(dict(list(sorted_inventory.values())[i]).values()); keys = sorted_inventory.keys()
        name = list(keys)[i]; price = values[0]; count = values[1]
        total_value += float(count*price)
        cost = "{:,.2f}".format(count * price)
        print(f"There are {count} {name}(s) worth ${cost}")
    _total = "{:,.2f}".format(total_value)
    print(f"The total value of the inventory is ${_total}")


def main():
    '''
    The main function of the program. Displays a menu asking the user for an option.
    '''
    msg = "Select option (1 to 4): "
    
    def display_menu():
        print("\r")
        print("(1) Add an item to the inventory")
        print("(2) Update an item in the inventory")
        print("(3) Print the items in the inventory with there values")
        print("(4) Quit")
        print("\r")
    inventory = {}

    selection = 0
    while True:
        try:
            if selection == 4: print("Goodbye"); break
            display_menu()
            selection = int(input(msg))
            if selection == 1: add_item(inventory)
            elif selection == 2: remove_item(inventory)
            elif selection == 3: calc_worth(inventory)
            elif selection == 4: print("Goodbye"); break
        except:
            while True:
                try:
                    selection = int(input("Invalid option. Please enter a number between 1 and 4: "))
                    if selection == 1 or selection == 2 or selection == 3 or selection == 4: break
                except:pass