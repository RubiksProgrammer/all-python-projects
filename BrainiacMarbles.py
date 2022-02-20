import random

#creating the game board function
def gameboard():
	board = [0]*11

	#generating gameboard values
	for i, r in enumerate(board):
		if i in [0, 1, 9, 10]:
			board[i] = [0] * 11
		elif i in [2, 3, 7, 8]:
			board[i] = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
		else:
			board[i] = [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]

	#set other starting positions on board
	board[5][7] = 2
	board[6][6] = 2
	board[7][6] = 2

	return board

games = []

#while loop that plays each game
while(True):

	board = gameboard()
	moves = []

	#while loop for selecting spots to move
	while(True):
		
		openSpots = []

		#get the open spots there are to move
		for indexR, r in enumerate(board):
			for indexC, c in enumerate(r):
				if c == 2:
					if board[indexR - 1][indexC] == 1 and board[indexR-2][indexC] == 1:

						openSpots.append((indexR, indexC, "U"))
					
					if board[indexR + 1][indexC] == 1 and board[indexR+2][indexC] == 1:
					
						openSpots.append((indexR, indexC, "B"))
					
					if board[indexR][indexC - 1] == 1 and board[indexR][indexC-2] == 1:
					
						openSpots.append((indexR, indexC, "L"))
					
					if board[indexR][indexC + 1] == 1 and board[indexR][indexC+2] == 1:
					
						openSpots.append((indexR, indexC, "R"))
		
		#if no spots left, exit out of loop
		if len(openSpots) == 0:
			break

		#select random move							
		choice = random.randint(0, len(openSpots)-1)
		moves.append(openSpots[choice])

		#execute move
		row, col, m = openSpots[choice]
		board[row][col] = 1

		if m == "U":
			board[row-1][col] = 2
			board[row-2][col] = 2
		elif m == "B":
			board[row+1][col] = 2
			board[row+2][col] = 2
		elif m == "L":
			board[row][col-1] = 2
			board[row][col-2] = 2
		elif m == "R":
			board[row][col+1] = 2
			board[row][col+2] = 2

	count = 0
	for r in board:
		for c in r:
			if c == 1:
				count += 1

	if count == 1:
		print(moves)
		print("GAME BEAT!!!!")
		break
	elif moves in games:
		continue
	else:
		print(moves)
		print(count)
		games.append(moves)
		continue















