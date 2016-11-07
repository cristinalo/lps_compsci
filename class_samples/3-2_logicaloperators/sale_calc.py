print("Enter amount of purchases, in cents:")
cents = int(raw_input())

if cents > 1000:
	total_discount = int(cents * float(.10))
	total_cost = int(cents - total_discount)
	print("You spent over $10! final price is " + str(total_cost) + " cents.")
if cents < 1000:
	print("you spent less than $10, there is no discount.")
