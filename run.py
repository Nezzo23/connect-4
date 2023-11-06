import numpy as np


# Creating a board needed for the game. Table 6*7

def playing_board():
    board = np.zeros ((6,7))
    return board

def drop_coin(board, row, col, coin):
    board[row][col] = coin

def valid_location(board, col):
    return board[5][col] == 0

def next_open_row(board, col):
    for row in range(6):
        if board[row][col] == 0:
            return row

def winning_move(board, coin):
    # Check horizontal 
    for col in range(4):
        for row in range(6):
            if (
                board[row][col] == coin
                and board[row][col + 1] == coin
                and board[row][col + 2] == coin
                and board[row][col + 3] == coin
            ):
                return True

    # Check vertical 
    for col in range(7):
        for row in range(3):
            if (
                board[row][col] == coin
                and board[row + 1][col] == coin
                and board[row + 2][col] == coin
                and board[row + 3][col] == coin
            ):
                return True

    # Check diaganols
    for col in range(4):
        for row in range(3):
            if (
                board[row][col] == coin
                and board[row + 1][col + 1] == coin
                and board[row + 2][col + 2] == coin
                and board[row + 3][col + 3] == coin
            ):
                return True

    for col in range(4):
        for row in range(3, 6):
            if (
                board[row][col] == coin
                and board[row - 1][col + 1] == coin
                and board[row - 2][col + 2] == coin
                and board[row - 3][col + 3] == coin
            ):
                return True


board = playing_board()
game_over = False
turn = 0

print (board)

# Setup conditions for the game (with loops)

while not game_over:
    # p1
    if turn == 0:
        selection = int(input("Player 1, Select your column (0-6):"))
    # p2
    else: 
        selection = int(input("Player 2, Select your column (0-6):"))
    # alternation between p1 and p2
    turn += 1
    turn = turn % 2

