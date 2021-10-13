import random
markers = ['X', 'O']

# Prints the board 
board_patterns = {
    1: '   |   |   ',
    2: '___ ___ ___'
}

def display_board(board):
    print('\n')
    print(board_patterns[1])
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print(board_patterns[1])
    print(board_patterns[2])
    print(board_patterns[1])
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print(board_patterns[1])
    print(board_patterns[2])
    print(board_patterns[1])
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print(board_patterns[1])
    print('\n')

# test_board = ['#','X','O','X','O','X','O','X','O']
# display_board(test_board)

# returns players marker choice
def player_input():

    p1_marker = 0

    while p1_marker not in markers:
        p1_marker = input("Please choose your marker between X and O ").upper()
        print('\n')

    p2_marker = 'O' if p1_marker == 'X' else 'X'
    return  (p1_marker, p2_marker)


# Place players marker at selected position on the board 
def place_marker(board, marker, position):
    board[position - 1] = marker
    return board

# Checks if game has been won by a particular player
def win_check(board, mark):
    result = False
    
    # Horizontal check 
    if (board[0] == board[1] == board[2] == mark) or (board[3] == board[4] == board[5] == mark) or (board[6] == board[7] == board[8] == mark):
        result = True
    # Vertical check 
    elif (board[0] == board[3] == board[6] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark):
        result = True
    # Diagonal check 
    elif (board[0] == board[4] == board[8] == mark) or (board[2] == board[4] == board[6] == mark):
        result = True

    return result

# Checks if board is filled 
def full_board_check(board):
    is_full = True

    for col in board:
        if col not in markers:
            is_full = False
            break
    
    return is_full

# Checks if column is free on the board(has not been played)
def space_check(board, position):
    return board[position - 1] not in markers

# Prompts user to choose a column on the board to play 
def player_choice(board):
    position_choice = None
    is_position_free = False

    while position_choice not in range(1, 10) or not(is_position_free):
        position_choice = input('Please choose a position on the board to place your marker 1 - 9: ')

        if not(position_choice.isdigit()):
            print('Please choose a valid position on the board 1 - 9: ')
            continue
        
        position_choice = int(position_choice)

        is_position_free = space_check(board, position_choice)


        if not(is_position_free):
            print(f'Board position {position_choice} has been played.')
        
    return position_choice

# Asks if player wants to play again
def replay():
    is_play_again = None
    answer_choices  = ['Yes', 'No']

    while is_play_again not in answer_choices:
        is_play_again = input('Do yo want to play again (please answer Yes or No)? ').capitalize()

        if is_play_again not in answer_choices:
            print("Please provide a valid answer.")

    return is_play_again == 'Yes'

print('Welcome to Tic Tac Toe!\n')
board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def choose_first():
    return random.randint(1, 2)


# Initialize the game
while True:
    # Select first player randomly 
    player_turn = choose_first()
    print(f"Player {player_turn} is going to be playing first")

    m1, m2 = player_input()

    p1_marker = m1 if player_turn == 1 else m2
    p2_marker = m1 if player_turn == 2 else m2

    print(f"The game is about to start with player {player_turn} going first")

    winner = None
    game_on = True
    
    while game_on:
        display_board(board_list)
        pl_choice = None
        
        if player_turn == 1:
            player_turn = 2
            print('Player 1 turn')
            pl_choice = player_choice(board_list)
            place_marker(board_list, p1_marker, pl_choice)
            winner = '1' if win_check(board_list, p1_marker) else None
        else:
            player_turn = 1
            print('Player 2 turn')
            pl_choice = player_choice(board_list)
            place_marker(board_list, p2_marker, pl_choice)
            winner = '2' if win_check(board_list, p2_marker) else None

        if full_board_check(board_list):
            display_board(board_list)
            print('The game is a tie🥂')
            game_on = False
        elif winner:
            display_board(board_list)
            print(f'Player {winner} won the game')
            game_on = False

    board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if not replay():
        print("\nThanks for playing this interactive Tic Tac Toe game.")
        print("Gracias")
        break