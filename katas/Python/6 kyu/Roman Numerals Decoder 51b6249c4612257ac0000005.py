# https://www.codewars.com/kata/51b6249c4612257ac0000005
from collections import OrderedDict

mapping = OrderedDict([('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)])


def solution(roman):
    result = 0
    last = 1001
    for c in roman:
        current = mapping[c]
        result += current
        if last < current:
            result -= 2 * last
        last = current
    return result