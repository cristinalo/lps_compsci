import random
magicnumber = random.randint(1,1000)
print("I'm thinking of a number between 1 and 1000. Enter your guess!")
guess = 0
while guess != magicnumber:
	guess = int(raw_input())
	if guess > magicnumber:
		print("Nope, too high! Guess again.")
	elif guess < magicnumber:
		print("Nope, too low! Guess again.")
	else:
		print("Hooray, you won!")
		break
