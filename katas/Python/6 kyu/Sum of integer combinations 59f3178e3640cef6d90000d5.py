# https://www.codewars.com/kata/59f3178e3640cef6d90000d5
from itertools import chain, combinations_with_replacement


def find(arr,n):
    return sum(1 for sub in chain(combinations_with_replacement(arr, i) for i in range(1, len(arr) + 1)) for c in sub 
                   if sum(c) == n)
