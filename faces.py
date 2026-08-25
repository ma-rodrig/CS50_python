#  In a file called faces.py, implement a function called
# convert that accepts a str as input and returns that same
# input with any :) converted to  🙂 (otherwise known as a
# slightly smiling face) and any :( converted to 🙁
#  (otherwise known as a slightly frowning face).
# All other text should be returned unchanged.

def convert(word):
	if word == ":)":
		return "🙂"
	else:
		return "🙁"

def main():
	print("Enter your text: ", end="")
	text = input().split()
	for word in text:
		if word == ":)" or word == ":(":
			ind = text.index(word)
			text[ind] = convert(word)
	print ("text converted: ", end="")
	for word in text:
		print(word, end=" ")
	print("")


if __name__ == "__main__":
	main()
	