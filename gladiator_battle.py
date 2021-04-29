#built-in random integer generator for dice mechanics
from random import randint	

#LXML library for parsing and writing XML data
from lxml import etree
import xml.etree.ElementTree as ET	

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

def roll_stats():
	#initialize the stats list and loop counter variables
	#stat_list is where the summed dice rolls will be stored
	stat_list = []
	loop_count = 1
	while loop_count <= 6:
		
		#initialize the roll list and loop counter variables
		#roll_list is used to store the dice rolls
		roll_list = []
		roll_count = 1
		
		#this flow follows the DnD mechanic of removing the lowest roll from the summation
		while roll_count <= 4:
			roll_count += 1
			dice_roll = roll_dice('d6',1,'sum')
			roll_list.append(dice_roll)
		
		#the final list of dice rolls is sorted in descending order and the lowest value is popped off
		roll_list.sort(reverse=True)
		roll_list.pop()
		stat_list.append(sum(roll_list))
		loop_count += 1
	
	stat_list.sort(reverse=True)

	#note that the value has to be returned so python doesn't assign its type as 'none'
	return stat_list

def modify_attr(attr_score):
	#this function takes the raw attribute score as an input and returns the modified score
	#it can accept strings and integers, but it will always return that form to the user
	#consider refactoring this function as a method after learning more about it in class
	flag_str = False
	flag_int = False

	#checks if the input was a string or integer and flags accordingly
	if type(attr_score) == str:
		flag_str = True
	elif type(attr_score) == int:
		flag_int = True

	#performs the math (note that converting to int automatically rounds 0.5 down)
	attr_score = int(attr_score)
	mod_score = (attr_score - 10)/2

	#this checks if the modifier divides evenly
	#the purpose of this is effectively to round numbers down since int()  doesn't always return the expected value
	if mod_score % 1 != 0:
		mod_score -= 0.5 

	#this needs to be performed or else the str() function returns the leading zero
	mod_score = int(mod_score)

	if flag_str == True:
		return str(mod_score)
	elif flag_int == True:
		return int(mod_score)

def build_stats(stat_list):
	#initialize the stats dictionary
	#stats_order is used because the dictionary is unordered by virtue of the object type
	#consider refactoring method this with a more efficient object or method
	stat_order = ['STR','DEX','CON','INT','WIS','CHA']
	stat_dict = {
	'STR':'',
	'DEX':'',
	'CON':'',
	'INT':'',
	'WIS':'',
	'CHA':''
	}

	#this index variable will be used to pull reference strings from the stats_order list
	stat_index = 0

	#this control flow iterates through the stats list in descending order
	for stat_score in stat_list:
		
		#communicate to the player what score is up for assignment

		#this control flow validates the selection is within range and has not already been selected
		selection_status = False
		while selection_status == False:
			
			#checks if the selection is within range and numeric
			player_selection = input(f'Assign your score of {stat_score} according to the numbered attribute list: ')
			selection_status = validate_selection_range(player_selection, 6)

			#this is a special use-case that only sees use in this stats building function
			#the general method can be abstracted into something that works more universally if needed
			if selection_status == True:
				# if the selection is valid then determine the key value that the player selected for score assignment
				dict_key = stat_order[int(player_selection) - 1]
				dict_val = stat_dict[dict_key]

				#if the key value is empty then permit assignment by exiting the control flow
				if dict_val == '':
					player_selection = True
				#if the key value is not empty but the player selection is otherwise valid then tell the player to select something different
				elif dict_val != '':
					selection_status = False
					print('Select an attribute that has not already been selected')
			
			#if the previous selection was out of range or not numeric then keep the selection status as false and do nothing else
			elif dict_val != '' and selection_status == False:
				selection_status = False

		#the validated selection is assigned to the dictionary
		stat_dict[dict_key] = stat_score

		#show the player the current assignments
		print('\n')
		display_stats(stat_dict)
		print('\n')

		#increment the stats index value
		stat_index += 1
	return stat_dict

def display_stats(stats_dict):
	str_atr = stats_dict['STR'] 
	dex_atr = stats_dict['DEX'] 
	con_atr = stats_dict['CON'] 
	int_atr = stats_dict['INT'] 
	wis_atr = stats_dict['WIS'] 
	cha_atr = stats_dict['CHA'] 

	print('NO.' + '\u2502' + 'ATR' + '\u2502' + 'SCR\n' +\
		'\u2500' * 3 + '\u253c' + '\u2500' * 3 + '\u253c' + '\u2500' * 3 + '\n' \
		' 1 ' + '\u2502' + 'STR' + '\u2502' + f'{str_atr}  \n' \
		' 2 ' + '\u2502' + 'DEX' + '\u2502' + f'{dex_atr}  \n' \
		' 3 ' + '\u2502' + 'CON' + '\u2502' + f'{con_atr}  \n' \
		' 4 ' + '\u2502' + 'INT' + '\u2502' + f'{int_atr}  \n' \
		' 5 ' + '\u2502' + 'WIS' + '\u2502' + f'{wis_atr}  \n' \
		' 6 ' + '\u2502' + 'CHA' + '\u2502' + f'{cha_atr}  ' )

def display_character_build(character_data):
	#parse the character data file and establish its root variable
	tree = etree.parse(character_data)
	root = tree.getroot()

	#assign the character data to a variable
	branch = root.find('character')
	name_branch = branch.find('name')
	branch = root.find('stats')
	lvl_branch = branch.find('level')
	char_name = pad_string(name_branch.text.capitalize() + ', LVL ' + lvl_branch.text.capitalize(), 27, True)

	#assign the character race and class data to a variable
	#consider refactoring the XML data structure, which would take one full session to do
	#changes would cascade to other areas of the code including validation
	#also need to consider the possibility of adding new classes, which would trigger simple refactoring
	branch = root.find('character')
	branch = branch.find('race')
	char_race = pad_string(branch[0].tag.capitalize() + ' Warrior', 27, True)

	#assign the HP data to a variable
	branch = root.find('stats')
	branch = branch.find('hp')
	char_hp = pad_string(branch.text, 2, False)

	#assign the speed data to a variable
	branch = root.find('stats')
	branch = branch.find('speed')
	char_sp = pad_string(branch.text, 2, False)

	#assign the attributes to an ordered list
	stat_list =[]
	mod_list = []
	branch = root.find('attribute')
	for attr_score in branch:
		attr_score = pad_string(attr_score.text, 3, False)
		mod_score = modify_attr(attr_score)
		mod_score = pad_string(mod_score, 3, False)
		stat_list.append(attr_score)
		mod_list.append(mod_score)

	#print the variables and the character sheet
	print(f'\u250f' + '\u2501' * 27 + '\u2513\n' \
		'\u2503' + char_name + '\u2503\n' \
		'\u2503' + char_race + '\u2503\n' \
		'\u2503' + ' ' * 27 + '\u2503\n' \
		'\u2503' + ' ' * 27 + '\u2503\n' \
		'\u2503' + 'ATR' + '\u2502' + 'RAW' + '\u2502' + 'MOD' + ' ' * 2 + 'HP' + '\u2502' + 'AC' + '\u2502' + 'SP' + ' ' * 6 + '\u2503\n' \
		'\u2503' + '\u2500' * 3 + '\u253c' + '\u2500' * 3 + '\u253c' + '\u2500' * 3  + ' ' * 2 + '\u2500' * 2 + '\u253c' + '\u2500' * 2 + '\u253c' + '\u2500' * 2  + ' ' * 6 + '\u2503\n' \
		'\u2503' + 'STR' + '\u2502' + stat_list[0] + '\u2502' + mod_list[0] + ' ' * 2 + char_hp + '\u2502' + ' ' * 2 + '\u2502' + char_sp + ' ' * 6 + '\u2503\n' \
		'\u2503' + 'DEX' + '\u2502' + stat_list[1] + '\u2502' + mod_list[1] + ' ' * 16 + '\u2503\n' \
		'\u2503' + 'CON' + '\u2502' + stat_list[2] + '\u2502' + mod_list[2] + ' ' * 2 + 'WEAPONS/ARMOR' + ' ' + '\u2503\n' \
		'\u2503' + 'INT' + '\u2502' + stat_list[3] + '\u2502' + mod_list[3] + ' ' * 16 + '\u2503\n' \
		'\u2503' + 'WIS' + '\u2502' + stat_list[4] + '\u2502' + mod_list[4] + ' ' * 16 + '\u2503\n' \
		'\u2503' + 'CHA' + '\u2502' + stat_list[5] + '\u2502' + mod_list[5] + ' ' * 16 + '\u2503\n' \
		'\u2503' + ' ' * 27 + '\u2503\n' \
		'\u2517' + '\u2501' * 27 + '\u251b')

def build_character():
	#start building the XML by declaring the root node
	#this variable will always be associated with the character_data.xml in this function
	root = etree.Element('root')

	#-----CHARACTER INFO-----#
	#create a node under root that contains character data
	character_branch = etree.SubElement(root, 'character')

	#name length validation loop
	selection_status = False
	while selection_status == False:	

		char_name = input('Name your gladiator: ')
		selection_status = validate_string_length(char_name, 25)

	#establish and write to the name tag
	branch = etree.SubElement(character_branch, 'name')
	branch.text = char_name

	#establish the race tag, call the list selector function, then write the selection
	branch = etree.SubElement(character_branch, 'race')
	race_tag = list_selection('race_data.xml', 'name')
	etree.SubElement(branch, race_tag)

	#-----STATS-----#
	#create a node under root that contains the stats data
	stats_branch = etree.SubElement(root, 'stats')

	#establish the attribute tag
	attribute_branch = etree.SubElement(root, 'attribute')

	#establish and write to the level tag
	#new players start at level 1
	branch = etree.SubElement(stats_branch, 'level')
	branch.text = '1'

	#establish and write to the XP tag
	#new players start at 0 XP
	branch = etree.SubElement(stats_branch, 'xp')
	branch.text = '0'

	#create a list of stats for the player to view and approve
	#the player has the option to keep or completely re-roll stats
	selection_status = True
	while selection_status == True:
		stat_list = roll_stats()
		print(stat_list)
		selection_status = yesno_selection('Re-roll stats? (Y/N): ')
	
	#build the stats dictionary and allow the user to re-build them at the end
	selection_status = True
	while selection_status == True:
		stat_dict = build_stats(stat_list)
		selection_status = yesno_selection('Re-select stats? (Y/N): ')	

	# #use this dictionary for spoofing stats for testing
	# stat_dict = {
	# 'STR':10,'DEX':10,'CON':10,'INT':10,'WIS':10,'CHA':10}

	#combine the race_data.xml and the recently-built stats_dict
	#the code also needs to recall the race that the player chose
	branch = root.find('character')
	branch = branch.find('race')
	
	#print the player-selected race 
	#this method is appropriate because there will only ever be one tag in this branch
	player_race = branch[0].tag

	#now the race_data.xml needs to be parsed
	race_data = ET.parse('race_data.xml')
	race_root = race_data.getroot()

	#find the corresponding race tag in the parsed XML and find the bonus tag
	branch = race_root.find(player_race)
	branch = branch.find('bonus')

	#now the code iterates through the stat_dict and searches the bonus branch for matching attributes
	for attr_key in stat_dict.keys():
		
		#search the race_data XML for the current attribute key
		#lower() method is used because all tags are written in undercase letters
		attr_tag = branch.find(attr_key.lower())

		#if no match is found etree returns None
		if attr_tag is None:
			pass
		#if a match is found then the bonus is added to the dictionary value
		else:
			#the XML text needs to be converted to integer type to be correctly summed
			stat_dict[attr_key] = stat_dict[attr_key] + int(attr_tag.text)

		#finally the stats are written to the character_data.xml file
		attr_branch = etree.SubElement(attribute_branch, attr_key.lower())

		#the stat is stored as a string because that is the oly accepted input for XML
		attr_branch.text = str(stat_dict[attr_key])

	#establish and write to the HP tag
	branch = etree.SubElement(stats_branch, 'hp')
	#roll the dice and add the consitution modifier to the result
	hp_raw = roll_dice('d12', 1, 'sum')
	hp_mod = modify_attr(int(stat_dict['CON']))
	branch.text = str(hp_raw + hp_mod)

	#establish the speed tag, recall the selected race, then write the movement speed
	branch = etree.SubElement(stats_branch, 'speed')
	speed = pull_value('race_data.xml', race_tag, 'speed')
	branch.text = speed

	#-----INVENTORY-----#
	#establish the inventory tag, call the list selector function, then write the selection
	inventory_branch = etree.SubElement(root, 'inventory')
	tag_name = list_selection('weapon_data.xml', 'name')
	etree.SubElement(inventory_branch, tag_name)

	#-----SAVE DATABASE-----#
	#once character building is complete the XML file is written
	et = etree.ElementTree(root)
	et.write('character_data.xml', pretty_print=True)		

def validate_selection_range(player_selection, upper_limit):
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

	#checks if the selection is within range
	if validation_status[0] == True and player_selection > 0  and player_selection <= upper_limit:
		validation_status[1] = True
	elif player_selection <= 0 or player_selection > upper_limit:
		print('Error: input was out of range')
		validation_status[1] = False
		return False

	#final validation check
	if all(validation_status) == True:
		return True

def validate_string_length(player_selection, char_limit):
	#validation status is assumed to be False unless proven to be true
	validation_status = False

	#checks if the character length exceeds the character limit
	if len(player_selection) > char_limit: 
		validation_status = False
		print(f'Error: input must be less than {char_limit} characters long')
		return False
	elif len(player_selection) <= char_limit:
		return True

def yesno_selection(message):
	player_ready = False
	#this control flow waits for the players to 'ready-up'
	while player_ready == False:
		ready_status = input(message).upper()
		if ready_status == 'Y':
			return True
		elif ready_status == 'N':
			#cannot return False because the loop breaks
			return False
		else:
			player_status = False
			print('Error: input must be Y or N')

def pull_value(data_list, parent_tag, child_tag):
#consider refactoring this function to accept an arbitrary number of inputs after the 'data_list' variable
	
	#this imports the data (i.e. parses it)
	tree = etree.parse(data_list)

	#this establishes the root node of the XML database
	root = tree.getroot()

	#this finds the parent tag and the subsequent child tag
	parent_tag = root.find(parent_tag)
	child_tag = parent_tag.findall(child_tag)
	return child_tag[0].text

def list_selection(data_list, tag_name):
#this function prints a list of elements that exist in an XML file
#the function receives the name of the data file and the tag that will be searched
#the function returns the parent of the node that matches the tag_name input	

	selection_list = []
	list_number = 1

	#this imports the data (i.e. parses it)
	tree = etree.parse(data_list)
	
	#this establishes the root node of the XML database
	root = tree.getroot()

	#begin the list printing
	print('Choose from the following: ')
	
	#this loop iterates through XML database and searches for the specified tag name
	#it stores the tags of the first-level data in a list
	for child in root.iter(tag_name):
		selection_list.append(child.text)
		print(f'{list_number}. {child.text}')
		list_number += 1

	#selection validation loop
	selection_status = False
	while selection_status == False:	

		list_selection = input('Player selection: ')
		selection_status = validate_selection_range(list_selection, len(selection_list))

	#returns the race tag text 
	#this is an lxml data type
	tag_name = root[int(list_selection) - 1]
	return tag_name.tag

def pad_string(input_string, field_length, adjustment):
	
	#determine the length of the string
	string_length = len(input_string)

	#determine if the string needs padding
	#if the input string is less than the field length then it needs to be padded
	if string_length < field_length:
		padding_delta = field_length - string_length

		#if the string is left-adjusted then the spaces are added on after
		if adjustment == True:
			input_string = input_string + padding_delta * ' '

		#if the string is right-adjsuted then the spaces are added on before
		elif adjustment == False:
			input_string = padding_delta * ' ' + input_string

		return input_string
	
	#otherwise the control flow is skipped	
	elif string_length == field_length:
		return input_string

#===========================================================================
#game loop
#===========================================================================
#tbd
#===========================================================================
#testing
#===========================================================================
# #this tests the functionality of the pull_value function
# #the inputs are the name of the data file, and the parent and child tag names
# #this should return a value of 25
# pull_value('race_data.xml', 'dwarf', 'speed')
# #this should return 'Half-Orc'
# pull_value('race_data.xml', 'halforc', 'name')

# #this tests the functionality of the score modifying function
# #the input is a single string or integer 
# #a score of 10 the function should return '0' (i.e. string)
# print(modify_attr('10'))
# #a score of 11 should also return '0'
# print(modify_attr('11'))
# #a score of 12 should return '1'
# print(modify_attr('12'))
# #a score of 9 should return '-1'
# print(modify_attr('9'))
# #a score of 8 should also return '-1'
# print(modify_attr('8'))
# #finally the data types need to be validated
# print(type(modify_attr('8')))
# print(type(modify_attr(8)))

# #this tests the functionality of the padding function
# #running this should pad an input string with empty space 
# #this is primarily to be used for maintiaining the appearance of the character sheet
# #the integer input is the total space that must be occupied
# #note that one space is expected
# test = pad_string('ABC', 10, True)
# print(test, 'end') 
# test = pad_string('XYZ', 3, True)
# print(test, 'end')

#this tests the functionalirt of the character sheet display function
#running this should produce a fully-populated character sheet for the plater to review
#the only input should be the character data file
display_character_build('rosebud_data.xml')

# # this tests the functionality of the character building function
# # running this should write the player inputs to the character_xml data file
# # used continually to test the function of the code as development progresses 
# build_character()

# #this tests the printout of the character stats and information
# #used as-needed to generate a reference image
# display_character_build()
# stats_dict = {
# 'STR':16,
# 'DEX':1,
# 'CON':'',
# 'INT':'',
# 'WIS':'',
# 'CHA':''
# }
# display_stats(stats_dict)

# #this tests the functionality of the user-input validation function
# #the function should behave similarly to the other selection validation function
# #it should return True or False
# #should be False
# validate_string_length('qwertyuiopasdfghjklzx', 20)
# #should be True
# validate_string_length('qwertyuiopasdfghjklz', 20)

# #this tests the functionality of the numeric input validation function
# #the function receives a numeric input 
# #then assesses if it's greater than zero and less than or equal to the limit
# #should be True
# validate_selection_rage('1',2)
# #should be True
# validate_selection_range('2',2)
# #should be False
# validate_selection_range('3',2)
# #should be False
# validate_selection_range('0',2)
# #this should be False
# validate_selection_range('A',1)

# #this tests the functionality of the list printing functiong
# #running this should print the items of an XML file as a list
# #the user should be prompted for an input that corresponds to the list
# #the function returns the tag name of a node
# list_selection('weapon_data.xml', 'name')

# # this tests the function of a die roller
# # it takes an input of a string value corresponding to the number of faces of a die
# # it also takes the quantity of dice
# # the function then determine if the player needs advantgage, disadvantage, or the sum
# # it returns the roll or sum of the rolls if multiple dice are used
# print(roll_dice('d20', 2, 'adv'))
# print(roll_dice('d20', 2, 'dis'))
# print(roll_dice('d100', 1, 'sum'))