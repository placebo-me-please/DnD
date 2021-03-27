#built-in random integer generator for dice mechanics
from random import randint	

#LXML library for parsing and writing XML data
from lxml import etree	

#clear the command line
import os
os.system('clear')

#===========================================================================
#functions
#===========================================================================
def roll_dice(faces, quantity, option):
#this function rolls dice
#it takes the number of faces, quantity, and scenario option (such as advantage) and outputs the roll result

	#initializes values
	roll_sum = 0
	roll_count = 1
	dual_roll = []

	#this is the dictionary of possible dice rolls
	dice_dict = {
	'd4' : 4,
	'd6' : 6,
	'd8' : 8,
	'd10' : 10,
	'd12' : 12,
	'd20' : 20,
	'd100' : 100
	}

	if option == 'sum':
		#a while loop is run a number of times equal to input quantity and is summed each time
		while roll_count < quantity + 1:
			#the code corelates the string value to the quantity then generates a random integer
			roll_sum = roll_sum + randint(1, dice_dict[faces])
			#increment the roll counter
			roll_count += 1

		#function is complete and outputs the sum of the rolls
		return roll_sum
	
	elif option == 'adv' or option == 'dis':
		#this will likely ever only be used with a d20, but other dice may be used without limitation
		#this chunk ignores whatever quantity is input because advantage/disadvantage die are only rolled twice
		dual_roll.append(randint(1, dice_dict[faces]))
		dual_roll.append(randint(1, dice_dict[faces]))
		
		#then return the lowest or highest of the two depending on the 'option' variable
		if option == 'adv':
			return max(dual_roll)
		elif option == 'dis':
			return min(dual_roll)

def display_character_build():
	print(f'\u250f' + '\u2501' * 27 + '\u2513\n' \
		'\u2503' + ' ' * 27 + '\u2503\n' \
		'\u2503' + ' ' * 27 + '\u2503\n' \
		'\u2503' + ' ' * 27 + '\u2503\n' \
		'\u2503' + ' ' * 27 + '\u2503\n' \
		'\u2503' + 'ATR' + '\u2502' + 'RAW' + '\u2502' + 'MOD' + ' ' * 2 + 'HP' + '\u2502' + 'AC' + '\u2502' + 'SP' + ' ' * 6 + '\u2503\n' \
		'\u2503' + '\u2500' * 3 + '\u253c' + '\u2500' * 3 + '\u253c' + '\u2500' * 3  + ' ' * 2 + '\u2500' * 2 + '\u253c' + '\u2500' * 2 + '\u253c' + '\u2500' * 2  + ' ' * 6 + '\u2503\n' \
		'\u2503' + ' ' * 3 + '\u2502' + ' ' * 3 + '\u2502' + ' ' * 7 + '\u2502' + ' ' * 2 + '\u2502' + ' ' * 8 + '\u2503\n' \
		'\u2503' + ' ' * 3 + '\u2502' + ' ' * 3 + '\u2502' + ' ' * 19 + '\u2503\n' \
		'\u2503' + ' ' * 3 + '\u2502' + ' ' * 3 + '\u2502' + ' ' * 5 + 'WEAPONS/ARMOR' + ' ' + '\u2503\n' \
		'\u2503' + ' ' * 3 + '\u2502' + ' ' * 3 + '\u2502' + ' ' * 19 + '\u2503\n' \
		'\u2503' + ' ' * 3 + '\u2502' + ' ' * 3 + '\u2502' + ' ' * 19 + '\u2503\n' \
		'\u2503' + ' ' * 3 + '\u2502' + ' ' * 3 + '\u2502' + ' ' * 19 + '\u2503\n' \
		'\u2503' + ' ' * 27 + '\u2503\n' \
		'\u2517' + '\u2501' * 27 + '\u251b')

def build_character():
	#start building the XML by declaring the root node
	root = etree.Element('root')

	#create a node under root that contains character data (rinse and repeat for other data)
	character_branch = etree.SubElement(root, 'character')

	#REFACTOR FLAG
	#need to establish a character limit so that the player card formats correctly
	char_name = input('Name your gladiator: ')
	name_branch = etree.SubElement(character_branch, 'name')
	name_branch.text = char_name
	
	#selection status is assumed to be false unless the validation function passes the user selection
	selection_status = False
	while selection_status == False:
		#this loop executes until the selection is recognized as valid
		
		#REFACTOR FLAG
		#move the list of possible options to wherever they are defined so that it's easier to add new races and classes
		print('\nChoose a race selection from the list below: \n' \
			'1. Human') 

		char_race = input('\nSelection: ')
		selection_status = validate_selection(char_race)
	race_branch = etree.SubElement(character_branch, 'race')
	#NEED TO CREATE THE ELEMENT DURING REFACTORING

	#selection status is assumed to be false unless the validation function passes the user selection
	selection_status = False
	while selection_status == False:
		#this loop executes until the selection is recognized as valid
		
		#REFACTOR FLAG
		#move the list of possible options to wherever they are defined so that it's easier to add new races and classes
		print('\nChoose a class selection from the list below: \n' \
			'1. Warrior') 

		char_class = input('\nSelection: ')
		selection_status = validate_selection(char_class)
	class_branch = etree.SubElement(character_branch, 'class')
	#NEED TO CREATE THE ELEMENT DURING REFACTORING

	#once character building is complete the XML file is written
	et = etree.ElementTree(root)
	et.write('character_data.xml', pretty_print=True)		

def validate_selection(player_selection):
	#validation statuses are assumed to be False unless proven to be True
	validation_status = [False, False]

	#checks if the value is numeric
	if player_selection.isdigit() == True:
		player_selection = int(player_selection)
		validation_status[0] = True
	elif player_selection.isdigit() == False:
		print('Error: input was not numeric')
		validation_status[0] = False
		return False

	#REFACTOR FLAG
	#this control flow should know the upper range limit based on the list it's pulling from
	#checks if the value is within range (only if it is numeric)
	if validation_status[0] == True and player_selection > 0  and player_selection < 2:
		validation_status[1] = True
	elif player_selection >= 0 or player_selection >= 10:
		print('Error: input was out of range')
		validation_status[1] = False
		return False

	#final validation check
	if all(validation_status) == True:
		return True

#===========================================================================
#game loop
#===========================================================================
#tbd
#===========================================================================
#testing
#===========================================================================
# #this tests the functionality of the character building function
# #running this should write the player inputs to the character_xml data file
# build_character()

#this tests the printout of the character stats and information
display_character_build()

# # this tests the function of a die roller
# # it takes an input of a string value corresponding to the number of faces of a die
# # it also takes the quantity of dice
# # the function then determine if the player needs advantgage, disadvantage, or the sum
# # it returns the roll or sum of the rolls if multiple dice are used
# print(roll_dice('d20', 2, 'adv'))
# print(roll_dice('d20', 2, 'dis'))
# print(roll_dice('d100', 1, 'sum'))
