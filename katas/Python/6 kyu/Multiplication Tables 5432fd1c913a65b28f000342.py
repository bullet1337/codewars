# https://www.codewars.com/kata/5432fd1c913a65b28f000342
def multiplication_table(row,col):
    return [[i * j for j in range(1, col + 1)] for i in range(1, row + 1)]