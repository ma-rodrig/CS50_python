# implement a program that prompts the user for a str of text and
# then outputs that same text but with all vowels (A, E, I, O, and U)
# omitted, whether inputted in uppercase or lowercase.


s = str(input('Input: '))
c = 0
is_vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

print("Output: ", end='')

for c in s:
	if (c not in is_vowel):
		print(c, end='')
print('')