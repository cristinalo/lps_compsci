print("Welcome to PumaPix!")
print("Enter your 5 favorite TV shows")
shows = 0
favs = []
while shows < 5:
	print("Enter your show name:")
	tv = raw_input()
	favs.append(tv)
	shows = shows + 1

print("Ok, here's what you entered:" + str(favs))
print("We have added better shows")

bettershows = ["Breaking Bad", "The Wire"]
together = favs + bettershows
together.sort()
y = 0
for x in together:
	y = y + 1
	print(str(y) + "." + x)

