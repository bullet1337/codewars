# https://www.codewars.com/kata/58ad317d1541651a740000c5
from math import factorial, ceil


def middle_permutation(string):
    half = factorial(len(string)) // 2
    string = sorted(string)
    result = ''
    i = len(string) - 1
    while half > 0:
        fact = factorial(i)
        div = int(ceil(half / fact))
        result += string[div - 1]
        string = string[:div - 1] + string[div:]
        half -= fact * max((div - 1), 1)
        i -= 1
    return result + ''.join(string)