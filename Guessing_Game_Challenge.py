from random import randint

print('Welcome to the Guessing Game!!!')
print('This program chooses a random number between 1 and 100, and you have to guess that number.\n')
print('Rules:')
print('1. If your guess is less than 1 or greater than 100, I will say "OUT OF BOUNDS"')
print('2. On your first turn, if your guess is:')
print('\t- within 10 of the number, I return "WARM!"')
print('\t- further than 10 away from the number, I return "COLD!"')
print('3. On all subsequent turns, if your guess is:')
print('\t- closer to the number than the previous turn, I return "WARMER!"')
print('\t- farther from the number than the previous turn colder, I return "COLDER!"')
print('4. When you guess the number, you will win the game and I will tell you how many guesses it took you.\n')
print('Good Luck!')


while True:
	num = randint(1,100)
	guesses = []
	while True:
		guess = int(input('Please enter a number between 1-100 as your guess:'))
		if int(guess) > 100 or int(guess) < 1:
			print("Not a valid guess") 
			continue
		else:
			guesses.append(guess)
		if guesses[-1] == num:
			print(f"You are right! The right number was {num}! It took you {len(guesses)} guesses!")
			break	
		elif len(guesses) == 1:
			if guesses[0] in range(num-10, num+11):
				print('WARM')
			else:
				print('COLD')
		elif abs(guesses[-1] - num) < abs(guesses[-2] - num):
			print('WARMER')
		elif abs(guesses[-1] - num) > abs(guesses[-2] - num):
			print('COLDER')
		elif guesses[-1] == guesses[-2]:
			print('Your guess is the same as before.')
	
	replay = input('Do you want to play again? Enter y or n:')
	if replay.upper() == 'Y':
		continue
	else:
		print('Thanks for playing the Guessing Game!')
		break





