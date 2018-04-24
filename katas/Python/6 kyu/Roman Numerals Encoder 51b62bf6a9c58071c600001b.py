# https://www.codewars.com/kata/51b62bf6a9c58071c600001b
from collections import OrderedDict


mapping = OrderedDict([('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)])
nearest_ten = {
    1000: 'C',
    500: 'C',
    100: 'X',
    50: 'X',
    10: 'I',
    5: 'I',
    1: ''
}


def solution(n):
    result = ''
    for l, v in mapping.items():
        div, n = divmod(n, v)
        result += l * div
        if n == 0:
            break

        ten = nearest_ten[v]
        if n >= v - mapping[ten]:
            result += ten + l
            n %= mapping[ten]

        if n == 0:
            break
    return result

    
    