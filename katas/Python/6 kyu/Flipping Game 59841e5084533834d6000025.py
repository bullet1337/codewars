# https://www.codewars.com/kata/59841e5084533834d6000025
import itertools


def flipping_game(num):
    str_num = ''.join(str(bit) for bit in num)
    return max((str_num[:slice[0]] + bin(int(str_num[slice[0]:slice[1]], 2) ^ (2 ** (slice[1] - slice[0]) - 1))
                + str_num[slice[1]:]).count('1') for slice in itertools.combinations(range(len(num) + 1), 2))