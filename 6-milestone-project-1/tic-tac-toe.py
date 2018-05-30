def display_board(board):
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('----|----|----')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----|----|----')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])


test_board = ['--', '--', '--', '--', '--', '--', '--', '--', '--']

display_board(test_board)
print('################')


def select_marker():
    value = ''
    while value != 'X' and value != 'O':
        value = input("Please pick a marker 'X' or 'O' : ")

    return value


def select_position():
    position = 0
    while position < 1 or position > 9:
        position = int(input("Please pick a position [1-9]: "))

    return position


def place_marker(board, marker, position):
    board[position - 1] = marker
    pass


selected_marker = select_marker()
selected_position = select_position()
place_marker(test_board, selected_marker, selected_position)
display_board(test_board)
