# https://www.codewars.com/kata/54ba84be607a92aa900000f1
from collections import Counter


def is_isogram(string):
    return all(v <= 1 for v in Counter(string.lower()).values())