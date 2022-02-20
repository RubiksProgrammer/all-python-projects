import random
#Display the board
def display_board(board):
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print('---------')
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print('---------')
    print(f"{board[7]} | {board[8]} | {board[9]}")

#Ask if want to be x or o
def player_input():
    marker = input("Player 1: Do you want to be X or O? ").upper()
    while marker not in ['X','O']:
        print('That is not a valid choice.')
        marker = input("Player 1: Do you want to be X or O? ").upper()
    if marker == 'X':
    	return {'Player 1': 'X', 'Player 2': 'O'}
    else:
    	return {'Player 1': 'O', 'Player 2': 'X'}

#Check if ready to play
def ready_check():
	ready = input('Are you ready to play? Enter Y or N: ')
	while ready not in ['Y', 'N']:
		print('That is not a valid answer.')
		ready = input('Are you ready to play? Enter Y or N: ')
	return ready == 'Y'

#Choose the first player
def choose_first():
    chooser  = random.randint(0,1)
    if chooser == 0:
        return ["Player 1", "Player 2"]
    else:
        return ["Player 2", "Player 1"]

#Check if a space is available
def space_check(board, position):
    return board[position] == ' '

#Ask for where the player wants to place their marker
def player_choice(board, playernum):
    while True:
        position = input(f"{playernum}: Please enter your next position as a number 1-9: ")
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('That is not a valid choice.')
            position = input(f"{playernum}: Please enter your next position as a number 1-9: ")
        if space_check(board, int(position)):
            break
        else:
            print("That position is already taken.")
    return int(position)

#Put the marker at a specific position on the board
def place_marker(board, marker, position):
    board[position] = marker

#Check if board is full
def full_board_check(board):
    return ' ' not in board

#Check if someone has won
def win_check(board, mark):
    testcases = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    markpositions = []
    for index,item in enumerate(board):
        if item == mark:
            markpositions.append(index)
    for case in testcases:
        if set(case).issubset(set(markpositions)):
            return True
    return False

#Ask if you want to replay
def replay():
    playagain = input("Do you want to play again? Enter Y or N: ")
    while playagain not in ['Y', 'N']:
        print('That is not a valid answer.')
        playagain = input("Do you want to play again? Enter Y or N: ")
    return playagain == 'Y'


print("Welcome to Tic-Tac-Toe!")

while True:

	board = [0, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

	players = choose_first()
	player1 = players[0]
	player2 = players[1]

	markers = player_input()
	marker1 = markers[player1]
	marker2 = markers[player2]

	print(f'{player1} will go first.')

	if not ready_check():
		continue

	display_board(board)

	while True:

		player1choice = player_choice(board, player1)
		place_marker(board, marker1, player1choice)
		display_board(board)

		if win_check(board, marker1):
			print(f"{player1} has won!!!!")
			break
		elif full_board_check(board):
			print("There was a draw!!!")
			break

		player2choice = player_choice(board, player2)
		place_marker(board, marker2, player2choice)
		display_board(board)

		if win_check(board, marker2):
			print(f"{player2} has won!!!!")
			break

	if not replay():
		print("Thanks for playing!!!")
		break

'''
display_board
player_input
ready_check
choose_first
space_check
player_choice
place_marker
full_board_check
win_check
replay

reset board
decide player one, player two
decide markers for each
play or not

player one is asked for spot
change made to board
new board displayed
check if someone wins
elif board is full than break and say there was a tie
player two is asked for spot
change made to board
new board is displayed
check if won

replay
'''














