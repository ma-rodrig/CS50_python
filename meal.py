#  implement a program that prompts the user for a time and outputs
# whether it’s breakfast time, lunch time, or dinner time. If it’s
#  not time for a meal, don’t output anything at all.

def main():
	the_time = input('What time is it?').strip()
	time = convert(the_time)
	if 7 <= time and time <= 8:
		print('breakfast time')
	elif 12 <= time and time <= 13:
		print('lunch time')
	elif 18 <= time and time <= 19:
			print('dinner time')

def convert(time):
	hours, minutes = time.split(':')
	converted_time = float(hours)+(float(minutes)/60)
	return converted_time

if __name__ == "__main__":
	main()