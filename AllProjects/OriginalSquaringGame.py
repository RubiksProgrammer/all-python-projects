from random import randint
from time import time

def whattype():
	while True:
		try: numtype = int(input("What type of questions do you want to answer? Enter:\n'1' for 2d*1d multiplication\n'2' for 3d*1d multiplication\n'3' for 2d*2d multiplication\n'4' for 2d squaring" +\
		"\n'5' for 3d squaring\n'6' for 2d+2d addition\n'7' for 3d+2d addition\n'8' for 3d+3d addition\n'9' to quit game\nEnter your answer here: "))
		except:
			print('That is not one of the options. Please select a number between 1-8: ')
		else:
			break
	return numtype

def problems(numtype):
	factor1 = [randint(10,99), randint(100,999)]
	factor2 = [randint(2,9), randint(10,99), randint(100,999)]

	if numtype == 1:
		print(f"What is {factor1[0]} times {factor2[0]}?")
		return factor1[0] * factor2[0]
	elif numtype == 2:
		print(f"What is {factor1[1]} times {factor2[0]}?")
		return factor1[1] * factor2[0]
	elif numtype == 3:
		print(f"What is {factor1[0]} times {factor2[1]}?")
		return factor1[0] * factor2[1]
	elif numtype == 4:
		print(f"What is {factor1[0]} squared?")
		return factor1[0]**2
	elif numtype == 5:
		print(f"What is {factor1[1]} squared?")
		return factor[1]**2
	elif numtype == 6:
		print(f"What is {addend1[0]} plus {addend2[1]}?")
		return addend1[0] + addend2[1]
	elif numtype == 7:
		print(f"What is {addend1[1]} plus {addend2[1]}?")
		return addend1[1] + addend2[1]
	elif numtype == 8:
		print(f"What is {addend1[1]} plus {addend2[2]}?")
		return addend1[1] + addend2[2]

def answer(number):
	while True:
		while True:
			try:
				myanswer = int(input("Enter your answer here: "))
			except:
				print("That is not an integer")
			else:
				break
		if myanswer == number:
			print('You got the answer right!')
			break
		else:
			print("Wrong answer! Try again.")

def replay():
	question = input("Press enter for next problem or c to change the problem.\nEnter your answer here: ")

	while question.lower() != '' and question.lower() != 'c':
		print('That is not a valid answer!')
		question = input("Press enter for next problem or c to change the problem.\nEnter your answer here: ")
	if question.lower() == "":
		return True
	else:
		return False
			
if __name__ == "__main__":
	while True:
		numtype = whattype()
		if numtype == 9:
			print("Thanks for playing!")
			break
		while True:
			t = time()
			number = problems(numtype)
			answer(number)
			print(f'It took you {time() - t:2.2f} seconds.')
			if not replay():
				break


