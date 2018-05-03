# https://www.codewars.com/kata/53db96041f1a7d32dc0004d2
import numpy as np


def done_or_not(board):
    for row in board:
        for element in row:
            if type(element) != int or element < 1 or element > len(board):
                return 'Try again!'

    board = np.array(board)

    for i in range(board.shape[0]):
        if len(set(board[i, :])) != board.shape[0] or len(set(board[:, i])) != board.shape[0]:
            return 'Try again!'

    for i in range(3):
        for j in range(3):
            if len(set(board[i * 3:(i + 1) * 3,
                             j * 3:(j + 1) * 3].flatten())) != board.shape[0]:
                return 'Try again!'
    
    return 'Finished!'