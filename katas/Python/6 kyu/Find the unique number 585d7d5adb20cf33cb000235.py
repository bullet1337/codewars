# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
from collections import Counter


def find_uniq(arr):
    return next(k for k, v in Counter(arr).items() if v == 1)