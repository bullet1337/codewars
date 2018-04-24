# https://www.codewars.com/kata/523f5d21c841566fde000009
def array_diff(a, b):
    b = set(b)
    return [x for x in a if x not in b]