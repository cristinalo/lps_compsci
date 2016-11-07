fave = 27
print("Try to guess my favorite number.")
number = int(raw_input())

if number > fave:
	print("Sorry, you lose. Try again: Next time use a lower number.")
if number < fave:
	print("Sorry, you lose. Try again: Next time use a higher number.")
if number == fave:
	print("Wow, you guessed it! You must be a genuis.")
