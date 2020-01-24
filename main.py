"""
Greg Lundberg
94283312
1/23/20

truffle manager is state of the art inventory management for the truffle
industry - disguised as exercise in functional decomposition.

parallel arrays of items and corresponding quantities are passed in. a main
menu is displayed, prompting the user to select among options to Order, Restock
or View the inventory. inventory data is used to generate submenus in which
item quantities are adjusted.

a set of base functions is created to handle menu display, user input,
input validation. these are composed in get_opt(), which provides the menus
with a single function to display their options and return a valid selection
from the user.

"""
items = ['Milk chocolate', 'Dark chocolate', 'Hazelnut']
quantities = [1000, 1000, 1000]


def truffle_man(items,quantities):

	options = ['ORDER', ' RESTOCK', ' PRINT', ' QUIT']

	opt = get_opt(options, lambda x: 0 <= x <= len(options))

	if opt == 1:
		order(items, quantities)
	elif opt == 2:
		restock(items, quantities)
	elif opt == 3:
		print_inventory(items, quantities)
	else:
		return items, quantities



# subtract quantity per order
def order(items, quantities):
	opt = get_opt(items, lambda x: 1 <= x <= len(items)) - 1
	num = get_opt(None, lambda x: 1 <= x, f'How many of {items[opt]}? ')

	if num <= quantities[opt]:
		quantities[opt] -= num
		print('Your order was successfully placed.\n')
	else:
		print("I'm sorry, your order could not be placed.\n")

	truffle_man(items, quantities)


# replenish quantity per order
def restock(items, quantities):
	opt = get_opt(items, lambda x: 1 <= x <= len(items)) - 1
	num = get_opt(None, lambda x: 1 <= x, f'How many of {items[opt]}? ')

	quantities[opt] += num
	print('That item has been restocked.\n')

	truffle_man(items, quantities)


# print table of inventory
def print_inventory(items, quantities):
	print('\n{:<20}{:<20}'.format('Item', 'Quantity'))
	for i in range(len(items)):
		print(f'{items[i]:20}{quantities[i]:<20}')

	truffle_man(items, quantities)


# composed function to handle menu display, input, validation
# returns 1-based index of menu options
def get_opt(options, validate_func, text='Please enter the number of your choice: '):
	if options:
		display(options)
	# prompt until valid selection
	opt = False
	while opt is False:
		opt = validate(prompt(text), validate_func)
	return opt


# prints n string args one per line
# list args passed to menu generator
def display(*args):
	for i in args:
		if type(i) == list:
			display_menu(i)
		else:
			print(i)


# prints numbered list as menu (1, 2...)
def display_menu(options):
	for i in range(len(options)):
		print(f'{i + 1}) {options[i]}')


# requests input from user
def prompt(text='Please enter the number of your choice: '):
	return input(text)


# check validity of input. return valid integer, otherwise False
def validate(val, func):
	val = int(val)
	if func(val):
		return val
	else:
		return False


truffle_man(items, quantities)