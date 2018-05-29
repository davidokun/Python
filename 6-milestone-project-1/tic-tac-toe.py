def display_board(board):
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('----|----|----')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----|----|----')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])


test_board = ['X1', 'O2', 'X3', 'O4', 'X5', 'O6', 'X7', 'O8', 'X9']

display_board(test_board)


def player_input():
    value = ''
    while value != 'X' and value != 'O':
        value = input("Please pick a marker 'X' or 'O' : ")

    return value


print(player_input())
