# https://www.codewars.com/kata/550498447451fbbd7600041c
from collections import Counter


def comp(array1, array2):
    return array1 is not None and array2 is not None and len(Counter(e ** 2 for e in array1) - Counter(array2)) == 0
	