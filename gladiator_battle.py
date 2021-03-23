#built-in random integer generator for dice mechanics
from random import randint		

#clear the command line
import os
os.system('clear')

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
		dual_roll[].append(randint(1, dice_dict[faces]))
		dual_roll[].append(randint(1, dice_dict[faces]))
		
		#then return the lowest or highest of the two depending on the 'option' variable
		if option == 'adv':
			return max(dual_roll)
		elif option == 'dis':
			return min(dual_roll)
		
#===========================================================================
#testing
#===========================================================================
#this tests the function of a die roller
#it takes an input of a string value corresponding to the number of faces of a die
#it also takes the quantity of dice
#the function then determine if the player needs advantgage, disadvantage, or the sum
#it returns the roll or sum of the rolls if multiple dice are used
# print(roll_dice('d4', 4, 'adv'))
# print(roll_dice('d8', 3, 'dis'))
# print(roll_dice('d100', 1, 'sum'))
