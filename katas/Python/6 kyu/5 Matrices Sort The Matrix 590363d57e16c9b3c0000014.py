# https://www.codewars.com/kata/590363d57e16c9b3c0000014
import itertools


def order(matrix):
    x = sorted(itertools.chain(*matrix))
    return [x[i::len(matrix)] for i in range(len(matrix))]