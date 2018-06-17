# https://www.codewars.com/kata/557af9418895e44de7000053
def repeat_it(s, n):
    return s * n if isinstance(s, str) else 'Not a string'