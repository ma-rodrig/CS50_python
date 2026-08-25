# implement a program that prompts the user for an arithmetic expression
# and then calculates and outputs the result as a floating-point value
# formatted to one decimal place. Assume that the user’s input will be
# formatted as x y z, with one space between x and y and one space between
#  y and z, wherein: x is an integer; y is +, -, *, or /; z is an integer

prompt = input('Expression: ').split(" ")

x = float(prompt[0])
y = prompt[1]
z = float(prompt[2])

if y == '+':
	print(f"{x+z:.1f}")
elif y == '-':
	print(f"{x-z:.1f}")
elif y == '*':
	print(f"{x*z:.1f}")
elif y == '/':
	print(f"{x/z:.1f}")