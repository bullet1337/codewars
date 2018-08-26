# https://www.codewars.com/kata/528d9adf0e03778b9e00067e
def mineLocation(field):
    return next([i, j] for i in range(len(field)) for j in range(len(field[i])) if field[i][j])