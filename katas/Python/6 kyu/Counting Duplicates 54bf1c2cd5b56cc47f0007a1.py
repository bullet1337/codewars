# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
from collections import Counter


def duplicate_count(text):
    print(text)
    return len([x for x in Counter(text.lower()).values() if x > 1])
     