import random
n = random.randint(0,20)
number_of_guess=0
while (number_of_guess<4):
	number_of_guess+=1
	x = int(input("Please enter a number between 0 and 20:\n"))
	if (n > x):
		print("Your guess is lower than the random number generated")
	elif (n < x):
		print("Your guess is higher than the random number generated")
	else:
		break
if (n == x):
	print("Congratulations, You guessed the correct number in" + " " + str(number_of_guess) + " " + "tries!")
else:
	print("Sorry, the random number generated is" + " " + str(n))