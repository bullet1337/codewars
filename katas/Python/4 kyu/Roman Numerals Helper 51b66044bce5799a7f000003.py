# https://www.codewars.com/kata/51b66044bce5799a7f000003
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


class RomanNumerals:

    @staticmethod
    def to_roman(n):
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

    @staticmethod
    def from_roman(str):
        result = 0
        last = 1001
        for c in str:
            current = mapping[c]
            result += current
            if last < current:
                result -= 2 * last
            last = current
        return result