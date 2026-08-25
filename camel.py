#  implement a program that prompts the user for the name of a
# variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.


def main():
    s = input("camelCase: ")
    print('snake_case: ', end='')
    snake = convert(s)
    print(' ')

def convert(s):
    for char in s:
        if char.isupper():
            print('_' + char.lower(), end='')
        else:
            print(char, end='')

main()