# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3
from collections import Counter


def find_uniq(arr):
    return next(s for i, s in enumerate(arr) if set(s.lower()) != set(arr[i - 1].lower()) and set(s.lower()) != set(arr[(i + 1) % len(arr)].lower()))