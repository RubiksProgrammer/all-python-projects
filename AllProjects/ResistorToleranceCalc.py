def ResistorToleranceCalc(resistance, tolerance):
	answer1 = resistance + (resistance*tolerance)
	answer2 = resistance - (resistance*tolerance)
	print (f"The tolerance of this resistor is from {answer2}Ω to {answer1}Ω.")

if __name__ == "__main__":
	while True:
		resistance = int(input("Enter resistance: "))
		tolerance = float(input("Enter tolerance: "))

		ResistorToleranceCalc(resistance, tolerance)

		replay = input("Press enter to continue or exit to exit.")

		if replay == "exit":
			break
		else:
			pass