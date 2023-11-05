import numpy as np


# Creating a board needed for the game. Table 6*7

def playing_board():
    board = np.zeros ((6,7))
    return board

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

