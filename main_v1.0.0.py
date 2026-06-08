import random
while True:
	# 1 = rock
	# 2 = paper
	# 3 = scissors
	random_choice = random.randint(0, 3)
	
	print("Rock paper scissors...")
	print("Your turn!")
	print("1 = Rock")
	print("2 = Paper")
	print("3 = Scissors")
	choice = int(input("Enter choice (1, 2, or 3): "))
	
	if random_choice == 1 and choice == 3:
		print("You win this round!")
	
	elif random_choice == 2 and choice == 1:
		print("You win this round!")
	
	elif random_choice == 3 and choice == 2:
		print("You win this round!")
	
	else:
		print("You lost this round")

