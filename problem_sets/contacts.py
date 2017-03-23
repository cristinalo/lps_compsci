number = True
contacts = {}
while number:
	print("Welcome to Contacts!")
	print("What would you like to do?")
	print("(1) Add a phone number.")
	print("(2) Print the full list of contacts.")
	print("(3) Enter a name to retrieve that contact's phone number.")
	print("(0) Exit the Contacts app.")
	response = int(raw_input())
	if response == 1:
		print("Enter the persons name and press enter")
		name = raw_input()
		print("Enter " + name + "phone number and press enter")
		numbers = raw_input()
		contacts[name] = numbers

	elif response == 2:
		print(contacts)
	elif response == 3:
		print("Enter a name and press enter")
		enter = raw_input()
		print(contacts[enter])
	elif response == 0:
		number = False
	
