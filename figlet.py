# implement a program that: Prompts the user for a str of text.
# Outputs that text in the desired font.

#If the user provides two command-line arguments and the first is
#  not -f or --font or the second is not the name of a font, the
# program should exit via sys.exit with an error message.

from pyfiglet import Figlet
from sys import argv, exit
from random import choice

figlet = Figlet()
font_list=figlet.getFonts()

if len(argv) == 1: #no font specified, random choice
	r_font = choice(font_list)
	figlet.setFont(font=r_font)

elif len(argv) == 3: #font specified, see if exists
	if argv[1]=='-f' or argv[1]=='--font':
		c_font = argv[2]
		if c_font not in font_list:
			exit('Invalid usage')
		figlet.setFont(font=c_font)
	else:
		exit('Invalid usage')
else:
	exit('Invalid usage')
text = input('Input: ')
print(figlet.renderText(text))
