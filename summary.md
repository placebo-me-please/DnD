*"Your first step in playing an adventure in the Dungeons & Dragon game is to imagine and create a character of your own."*

*Dungeons and Dragons PHB, Ed. 5*

## Summary ##

This is an extension of what I learned from creating the Tic-Tac-Toe game I had to build for my Python course. This wasn't motivated by anything really: I just enjoy Dungeons & Dragons, so I thought I would try to reproduce the character-building aspect of the game. The rules of building a character, let alone simulating combat and roleplaying, are more complex than the rules of Tic-Tac-Toe, so this project felt like a welcome challenge.

## User Story ##

The player runs the code and is prompted to provide their input. In some instances that input is a string, like a name; in others the input is a numeric selection from a list. Each input is validated before proceeding to the next prompt. If the user input is not correct then the code notifies them of their error.

In between selections, the code acceses and displays data stored in one of two XML files: one contains character race data, and the other contains weapon data. The player selections are written as elements and text for a third XML file that is written at the conclusion of the code. The XML file contains all of the selections made by the player. 

The final output of the code is visual display character sheet that resembles the offical template. The player can then easily inspect their attribute scores, item selections, etc. 

The code also incorporates some basic dice and attribute mechanics than can easily be recycled for extensions of this project.

Generally speaking, functions were created to be as abstract as possible. For example, a function that parses an XML file and searches for a specific element should be usable in any context for which the XML file is structured correctly.

## Future Use ##

The end-use of this code is TBD, but I learned enough from developing it that it surely has some value. For example, I learned how to use the ElemenTree API for parsing, reading, and writing XML files, which is a gateway into learning more about databases. Perhaps I'll be able to re-use some functions and methods from this code in a future project.

This could be used to create a printable character sheet for tabletop DnD, or I could create a gladiator combat scenario that increases in difficulty as the player progresses.
