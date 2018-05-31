import random

test_board = ['#', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']


def display_board(board):
    """
    Function that can print out a board.
    :param board:
    :return:
    """
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('----|----|----')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----|----|----')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    """
    Function that can take in a player input and assign their marker as 'X' or 'O'
    :return:
    """
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    """
    Takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9)
    and assigns it to the board.
    :param board:
    :param marker:
    :param position:
    :return:
    """
    board[position] = marker
    pass


def win_check(board, mark):
    """
    function that takes in a board and checks to see if someone has won.
    :param board:
    :param mark:
    :return:
    """
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    """
    Randomly decide which player goes first
    :return:
    """
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    """
    Returns a boolean indicating whether a space on the board is freely available.
    :param board:
    :param position:
    :return:
    """
    return board[position] == '  '


def full_board_check(board):
    """
    Checks if the board is full and returns a boolean value. True if full, False otherwise.
    :param board:
    :return:
    """
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    """
    Asks for a player's next position (as a number 1-9)
    :param board:
    :return:
    """
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    """
    Function that asks the player if they want to play again and returns a boolean True if they do want to play again.
    :return:
    """
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
