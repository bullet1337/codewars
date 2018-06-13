# https://www.codewars.com/kata/529eef7a9194e0cbc1000255
from collections import Counter


def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())