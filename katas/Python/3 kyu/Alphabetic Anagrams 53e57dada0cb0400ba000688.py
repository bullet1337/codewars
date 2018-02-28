# https://www.codewars.com/kata/53e57dada0cb0400ba000688
import operator
from functools import reduce
from itertools import groupby
from math import factorial


def combinations(counts):
    return factorial(sum(counts)) / reduce(operator.mul, (factorial(x) for x in counts))


def listPosition(word):
    position = 1
    letters = [[k, len(list(g))] for k, g in groupby(sorted(word))]
    for l in word:
        index = next(i for i, (letter, _) in enumerate(letters) if letter == l)
        for prev in letters[:index]:
            prev[1] -= 1
            position += combinations([e[1] for e in letters if e[1] != 0])
            prev[1] += 1
        letters[index][1] -= 1
        if letters[index][1] == 0:
            letters.pop(index)

    return position