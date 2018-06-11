# https://www.codewars.com/kata/57f6ad55cca6e045d2000627
def square_or_square_root(arr):
    return [x ** .5 if (x ** .5).is_integer() else x ** 2 for x in arr]