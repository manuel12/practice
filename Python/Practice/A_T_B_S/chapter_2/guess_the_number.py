# A short program: Guess the Number
# This is a guess the number game.

import random
secret_number = random.randint(1, 20)
print("I'm thinking on a number between 1 and 20.")

# Ask the player to guess six times.
for guesses_taken in range(1, 7):
	print("Take a guess.")
	guess = int(input())

	if guess < secret_number:
		print("Your guess is too low.")
	elif guess > secret_number:
		print("Your guess is too high.")
	else:
		break # This condition is the correct guess.

if guess == secret_number:
	print("Good job! you guess the righ number in " + str(guesses_taken) + " guesses!")
else:
	print("Nope the number I was thinking on was " + str(secret_number))

