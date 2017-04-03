class Player(object): 
  def __init__(self, name, age, goals, jersey_number, position): 
    self.name = name 
    self.age = age 
    self.goals = goals 
    self.jersey_number = jersey_number 
    self.position = position 
 
 # This block of code is used to have the summaries of the players that have been added to the team  
  def getSummary(self): 
    summary = "name: " + self.name + "\n" 
    summary = summary + "age: " + str(self.age) + "\n" 
    summary = summary + "goals: " + str(self.goals) + "\n" 
    summary = summary + "Jersey Number: " + str(self.jersey_number) + "\n" 
    summary = summary + "Position: " + str(self.position) + "\n" 

    return summary

# Saves the teams 
def saveTeam(myPlayers, filename):
        # Opens the file to write in it and save the data  
	crayola = open(filename, "a") 
	# Creates a loop so that all the players in the file are saved 
	for p in myPlayers: 
		crayola.write(p.name + " " + str(p.age) + " " + str(p.goals) + " " + str(p.jersey_number) + " " + p. position + " ")
 	# Closes the file 
	crayola.close() 

def loadTeam(filename):
	# creates an empty list 
	emptyList = []
	# open file to read it
	fileee = open(filename, "r")
	# read each line of the file
	lines = my_file.readline()
	# make a loop
	while lines != "":
		# split the lines of the file so it becomes a list
		myWords = lines.split()
		# add to the list 
		emptyList.append(Player(str(myWords[0]), str(myWords[1]), str(myWords[2]), str(myWords[3]), str(myWords[4]) + "\n"))
		# this adds something to every line that gets read 
		lines = fileee.readline()
	        # closes the file so that others can go in it
	        fileee.close()
	        # return whatever is in the list now
	        return emptyList  

  

keepRunning = True 

# ask the user what they want to do
print("Welcome to Team Manager Deluxe!")
print("Do you want to start with a new team or open an existing team?")
print("Enter the number of your choice")
print("(1) Start with a new team")
print("(2) Open a file for an existing team")
# the user can input what option they want
response = raw_input()

# option 2 will load a team file that is already made
if response == "2":
	# asks what the file name is
	print("What's the filename for your existing team? Enter the whole name, including its .tmd exetension")
	# this allowes them to write the file name
	filename = raw_input()
	# this prints whatever was in the file
	myPlayers = loadTeam(filename)
# option 1 will start of with a new team
else:
	myPlayers = []



# Different options for what the user can do  
while keepRunning: 
  print("What would you like to do? Enter your choice and press 'enter'.")
  print("(1) Add a player.") 
  print("(2) Print players.")
  print("(3) Save your player list to a file.")  
  print("(0) Leave the program.(save first to avoid losing your data!)") 
  
  response = input() 

# The program will stop running if they enter 0  
  if response == 0: 
    keepRunning = False 

# OPtion 1, lets them add the info to make a new player    
  elif response == 1: 
    print("Ok, enter the players name and press enter.") 
    name = raw_input()
    print("How old is the player?") 
    age = raw_input() 
    print("How many goals has this player scored?") 
    goals = raw_input() 
    print("What is the jersey number?") 
    jersey_number = raw_input()
    print ("What position does the player play?") 
    position = raw_input()
    
# adds the new player into the team 
    myPlayers.append(Player(name, age, goals, jersey_number, position))
   
    print("Ok, got it! View your players again to see it!")

# Gives info of players in the list  
  elif response == 2: 
    for p in myPlayers: 
      print(p.getSummary())

# it saves the players in a file 
  elif response == 3:
	# asks what they want to name it
	print("What will be the name of your file? Enter the name, including the .tmd extension.")
	filename = raw_input()
	# save their players and file based on what they named it
	saveTeam(myPlayers, filename)

      
 

