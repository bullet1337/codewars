# https://www.codewars.com/kata/54da5a58ea159efa38000836
from collections import Counter  


def find_it(seq):
    return next(k for k, v in Counter(seq).items() if v % 2 != 0)
