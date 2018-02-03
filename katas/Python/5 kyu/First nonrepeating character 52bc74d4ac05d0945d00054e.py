# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
	pass 


def first_non_repeating_letter(string):
    counter = OrderedCounter(string)
    return next((l for l, c in counter.items()
                 if c + (counter[l.upper() if l.islower() else l.lower()] if l.isalpha() else 0) == 1), '')