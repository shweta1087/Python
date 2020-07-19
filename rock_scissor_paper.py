import random

list = ['rock', 'scissor', 'paper']
computer = random.choice(list)
print("Value selected by system is",computer)

User=input("Select one of \"rock, paper, scissor\": \n")

if(computer == "rock"):
	if(User == "paper"):
		print("Congratulations, you won!!!")
	elif(User == "scissor"):
		print("Sorry, you lost!!! Value selected by computer is", computer)
	else:
		print("its a draw")

if(computer == "paper"):
	if(User == "scissor"):
		print("Congratulations, you won!!!")
	elif(User == "rock"):
		print("Sorry, you lost!!! Value selected by computer is", computer)
	else:
		print("its a draw")

if(computer == "scissor"):
	if(User == "rock"):
		print("Congratulations, you won!!!")
	elif(User == "paper"):
		print("Sorry, you lost!!! Value selected by computer is", computer)
	else:
		print("its a draw")
