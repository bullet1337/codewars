# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004
from collections import Counter
from itertools import groupby


def highest_rank(arr):
    counter = Counter(arr).most_common()
    return max(counter[i][0] for i in range(len(counter)) if counter[i][1] == counter[0][1])