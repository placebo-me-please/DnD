#built-in random integer generator for dice mechanics
from random import randint		

#clear the command line
import os
os.system('clear')

def roll_dice(faces, quantity):
	#initializes values
	roll_sum = 0
	roll_count = 1

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

	#a while loop is run a number of times equal to input quantity and is summed each time
	while roll_count < quantity + 1:
		#the code corelates the string value to the quantity then generates a random integer
		roll_sum = roll_sum + randint(1, dice_dict[faces])
		#increment the roll counter
		roll_count += 1

	#function is complete and outputs the sum of the rolls
	return roll_sum

#===========================================================================
#testing
#===========================================================================
#this tests the function of a die roller
#it takes an input of a string value corresponding to the number of faces of a die
#it also takes the quantity of dice
#it returns the roll or sum of the rolls if multiple dice are used
# print(roll_dice('d4', 2))
# print(roll_dice('d8', 3))
# print(roll_dice('d100', 1))