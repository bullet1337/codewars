# https://www.codewars.com/kata/540afbe2dc9f615d5e000425
from math import sqrt

import numpy as np



class Sudoku(object):

    def __init__(self, board):
        self.error = False
        for row in board:
            for element in row:
                if type(element) != int or element < 1 or element > len(board):
                    self.error = True

        self.board = np.array(board)

    def is_valid(self):
        if self.error:
            return False
            
        small_size = sqrt(self.board.shape[0])
        if not small_size.is_integer():
            return False
        small_size = int(small_size)

        for i in range(self.board.shape[0]):
            if len(set(self.board[i, :])) != self.board.shape[0] or len(set(self.board[:, i])) != self.board.shape[0]:
                return False

        for i in range(small_size):
            for j in range(small_size):
                if len(set(self.board[i * small_size:(i + 1) * small_size,
                                      j * small_size:(j + 1) * small_size].flatten())) != self.board.shape[0]:
                    return False

        return True
