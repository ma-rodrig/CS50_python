#  In a file called einstein.py, implement a program in Python
# that prompts the user for mass as an integer (in kilograms)
# and then outputs the equivalent number of Joules as an integer.
#  Assume that the user will input an integer.

# E = mc^2

def main():
	print("m: ", end="") #buscar o valor de m

	m = int(input())

	c = 3 * (10**8) #definir valor de c

	E = m *(c ** 2) #formula de calculo

	print ("E: ", E, end=" ") #printar resultado


if __name__ == "__main__":
	main()