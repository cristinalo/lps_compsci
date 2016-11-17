print("For what number would you like multiples?")
multiples = float(raw_input())
number = 0
count = 0
while count < 1000:
	count = multiples * number
	print(str(number) + " times " + str(multiples) + " equals " + str(count))
	number += 1
