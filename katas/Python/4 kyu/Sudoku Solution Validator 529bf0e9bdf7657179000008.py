# https://www.codewars.com/kata/529bf0e9bdf7657179000008
import numpy as np


def validSolution(board):
    board = np.array(board)

    for i in range(9):
        if len(set(board[i, :])) != 9 or len(set(board[:, i])) != 9:
            return False

    for i in range(3):
        for j in range(3):
            if len(set(board[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3].flatten())) != 9:
                return False

    return True
