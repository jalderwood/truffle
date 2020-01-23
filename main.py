"""
Greg L
94283312
1/21/20

truffle_manager demonstrates functional programming techniques through
simulation of an order-taking system for a truffle business.

an array of inventory record is passed in and used to generate a submenu
of the items in inventory. the user may select among options
to order items from the inventory, restock, or view the updated data
after return from the adjust() function, which is used for both
ordering and restocking.

"""


inventory = [["Milk chocolate", 1000], ["Dark chocolate", 1000], ["Hazelnut", 1000]]

# truffleManager is the control function which sets up the main menu
# and calls the other functions according to user input.
# it accepts an array of inventory in Record format
def truffle_manager(inv):

    mainMenu = ['ORDER', ' RESTOCK', ' PRINT', ' QUIT']

    while True:
        num = menu(mainMenu)
        if num == 0:
            inv = adjust(inv)
        elif num == 1:
            inv = adjust(inv, True)
        elif num == 2:
            show(inv)
        else:
            break  # can only be Quit (3)

    return inv


# menu accepts a list of inventory items and presents them to the user as
# numbered options (i+1). user will be prompted until a valid number is
# entered, which is then returned as the [zero-based] index of the item chosen.
def menu(options):
    while True:
        for i in range(len(options)):
            print(f'{i + 1}) {options[i]}')

        num = int(input('Please enter the number of your choice: ')) - 1  # adjust to index
        if num in range(0, len(options)):  # validate selection
            break

    return num


# adjust updates inventory data up or down according to orders or restocks.
# the restock flag determines the operation.
def adjust(inv, restock=False):
    # inventory items, qty's to separate arrays
    items = []
    quantities = []
    for i in inv:
        items.append(i[0])
        quantities.append(i[1])
    # item to be adjusted (0-based index)
    num = menu(items)

    while True:
        n = int(input(f'How many of {items[num]}? '))
        if n > 0:
            if restock:
                quantities[num] += n
                print('That item has been restocked.\n')
                break
            if n <= quantities[num]:
                quantities[num] -= n
                print('Your order was successfully placed.\n')
                break
            elif n > quantities[num]:
                print("I'm sorry, your order could not be placed.\n")
                break
    # reconstruct inventory data structure for  return
    arr = []
    for i in range(len(items)):
        arr.append([items[i], quantities[i]])
    return arr


# print inventory to console
def show(inv):
    print('{:<20}{:<20}'.format('Item', 'Quantity'))
    for i in inv:
        print(f'{i[0]:20}{i[1]:<20}')
    print('\n')


truffle_manager(inventory)