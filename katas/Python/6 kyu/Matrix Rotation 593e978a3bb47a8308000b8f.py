# https://www.codewars.com/kata/593e978a3bb47a8308000b8f
def rotate_clockwise(matrix):
    return [''.join(x) for x in zip(*reversed(matrix))]