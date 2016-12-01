# start off with print statement
print("These are our ice creams:")
# I have to add a variable and assign it characters
flavors = ["chocolate", "vanilla", "strawberry", "banana"]
# It will print out all of the flavors that i have assigned it to 
print(flavors)
print("Want to add an ice cream flavor? Enter it now:")
icecream = raw_input()
# It will ask for a flavor of your own & it will be a raw inout
print("Great! Here is our new menu:")
# this will make the flavors print in a list
for current_flavor in flavors:
	print(current_flavor)
# this will print the flavors in order with the raw input flavor at the end
print(icecream)
