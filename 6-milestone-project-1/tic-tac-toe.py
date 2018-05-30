def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('----|----|----')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----|----|----')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


# test_board = ['--', '--', '--', '--', '--', '--', '--', '--', '--']
test_board = ['#','X','O','X','O','X','O','X','O','X']


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
    board[position] = marker
    pass


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


selected_marker = select_marker()
selected_position = select_position()
place_marker(test_board, selected_marker, selected_position)
display_board(test_board)
print(win_check(test_board, selected_marker))
