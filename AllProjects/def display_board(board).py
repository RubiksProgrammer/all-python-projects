def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('----------')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('----------')
    print(f'{board[7]} | {board[8]} | {board[9]}')

def player_input():
    marker = input('Player 1: Do you want to be X or O? Please enter your choice here. ').upper()
    while marker != 'O' and marker != 'X':
        marker = input('Player 1: Do you want to be X or O? Please the right character. ').upper()
    if marker == 'X':
        marker1 = 'O'
    else:
        marker1 = 'X'
    return [marker,marker1]

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    rows = [board[1:4],board[4:7],board[7:10],board[1:8:3],board[2:9:3],board[3:10:3],board[1:10:4],board[3:8:2]]
    for lines in rows:
        if lines.count(mark) == 3:
            return True
    return False

from random import randint

def choose_first():
    signs = player_input()
    coin = randint(0,1)
    if coin == 0:
        print('Player 1 goes first.')
        return signs
    else:
        print('Player 2 goes first.')
        signs.reverse()
        return signs

def space_check(board, position):
     return board[position] == ' '

def full_board_check(board):
    return ' ' not in board

def player_choice(board):
    position = int(input('Choose your next position: (1-9) '))
    while position not in [1,2,3,4,5,6,7,8,9]  or not space_check(board, position):
        position = int(input('The position you chose is not available. Please choose a different position: (1-9) '))
    return position

def replay():
    play = input('Do you want to play again? Enter Yes or No. ')
    while play != 'Yes' and play != 'No':
        play = input('Do you want to play again? Please enter Yes or No. ')
    return play == 'Yes'

print('Welcome to Tic Tac Toe!')
while True:
    board = [0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
    markers = choose_first()
    display_board(board)
    
    while True:
        place_marker(board, markers[0], player_choice(board))
        display_board(board)

        if win_check(board, markers[0]):
            print(f'Congratulations! {markers[0]} has won the game!')
            break
        elif full_board_check(board):
            print('There was a draw!')
            break

        place_marker(board, markers[1], player_choice(board))
        display_board(board)
        
        if win_check(board, markers[1]):
            print(f'Congratulations! {markers[1]} has won the game!')
            break
        elif full_board_check(board):
            print('There was a draw!')
            break           

    if not replay():
        print('Thanks for playing!')
        break




