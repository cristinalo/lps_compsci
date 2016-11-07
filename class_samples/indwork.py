

print("How many miles do you live from Richmond State?")
miles = int(raw_input())

print("What is your GPA?")
GPA = float(raw_input())

if miles <= 30 and GPA >= 2.0:
	print("Hooray, you made it in!")
if miles <= 30 and GPA < 2.0:
	print("Sorry, just because you live close dosent mean you're automatically in!")
if miles > 30 and GPA < 2.5:
	print("Sorry, I hope this wasnt your first choice!")
if miles > 30 and GPA >= 2.5:
	print("What was your ACT score?")
	ACT = int(raw_input())
	if ACT < 32 and ACT >= 18:
		print("You barely made it!")
	elif ACT > 32:
		print("Lol, You're lying the highest ACT score is 32. Try again next year!")
	elif ACT < 18 or GPA < 2.5 or ACT > 32:
		print("You have been rejected, try again next year!")

