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
elif fork == 'right' and strength > 5:
	print("You were able to stop a boulder from crushing you thanks to those biceps!")
elif fork == 'right' and health <= 3:
	print(str(name) + " dont even try to go this way with that health! You have died from a heart attack.")
elif fork == 'right' and luck >= 6:
	print("You got lucky enough and ran away before the zombies had a chance to get you but your partner Glenn Saldy died :(")

if fork == 'left' and luck >= 5:
	print("You got lucky! You didnt get bitten by a spider but now you wont be able to turn into spider man :(")
elif fork == 'left' and luck <= 4:
	print("You are so unlucky, you have died from tripping on your own feet by getting chased by a bee")
elif fork == 'left' and health >= 5:
	print("You have survived not dying from a heart attack when Trump was declared President!")
elif fork == 'left' and strength >= 5:
	print("You were strong enough to break up a fight, good job") 
