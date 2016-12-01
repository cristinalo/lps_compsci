print("Welcome to Cristina's quest!")
print("What is the name of your character?")
name = raw_input()
print("Enter strength from 1-10")
strength = int(raw_input())
print("Enter health from 1-10")
health = int(raw_input())
print("Enter luck from 1-10")
luck = int(raw_input())
total = strength + health + luck

if total > 15:
	print("You have given your character too many points! Default values have been assigned, " + str(name) + " strength: 5, health: 5, luck: 5")
if total <= 15:
	print("You have given " + str(name) + " , strength: " + str(strength) + " health: " + str(health) + " luck: " + str(luck) + ".")
print(str(name) + " has come across a fork in the road! Do you want to go left or right? Enter 'right' or 'left'. ")
fork = raw_input()

if fork == 'right' and strength < 4:
	print("Oh No! A boulder has squished you! Eat more vegetables to be stronger next time!")
elif fork == 'right' and strength >= 5:
	print("You were able to stop a boulder from crushing you thanks to those biceps!")
if fork == 'right' and health <= 3:
	print("Lol, dont even try to go this way with that health! You have died from a heart attack.")
if fork == 'left' and luck >= 5:
	print("You have fallen into a trap but dont worry you were lucky enough to find a way out!")
elif fork == 'left' and luck < 5:
	print("You were not lucky enought to survive a spider bite! You wont be able to be spider man now :(")
