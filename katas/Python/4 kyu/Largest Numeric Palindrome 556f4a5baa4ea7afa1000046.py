# https://www.codewars.com/kata/556f4a5baa4ea7afa1000046
from itertools import combinations
from operator import mul
from collections import Counter


def numeric_palindrome(*args):
    args = [arg for arg in args if arg != 0]
    max_palindrome = 0
    for i in reversed(range(1, len(args))):
        for comb in combinations(args, i + 1):
            digits_count = Counter(str(reduce(mul, comb)))
            solo = ''
            for digit, count in digits_count.items():
                if count % 2 != 0:
                    solo = max(solo, digit)
            else:
                result = ''.join(digit * (count // 2) for digit, count in sorted(digits_count.items(), reverse=True))
                result += solo + result[::-1]
                if result[0] == '0':
                    result = result[digits_count[0]:-digits_count[0]]
                if result:
                    result = int(result)
                    if result > max_palindrome:
                        max_palindrome = result
    return max_palindrome
                    