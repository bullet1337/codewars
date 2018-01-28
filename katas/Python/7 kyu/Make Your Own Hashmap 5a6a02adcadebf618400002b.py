# https://www.codewars.com/kata/5a6a02adcadebf618400002b
from collections import defaultdict


def my_hash_map(list_of_strings):
    map = defaultdict(list)
    for string in list_of_strings:
        map[sum([ord(c) for c in string])].append(string)
    return map