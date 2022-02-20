if __name__ == "__main__":

	while True:
		try:
			number = int(input("Enter the number you want to check if it is prime: "))
		except:
			print(f"{number!r} is not an integer.")
