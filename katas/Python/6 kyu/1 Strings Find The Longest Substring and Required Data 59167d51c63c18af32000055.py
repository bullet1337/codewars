# https://www.codewars.com/kata/59167d51c63c18af32000055
import itertools


def find_longest_substr(s):
    start = 0
    char = None
    length = 0
    current_index = 0
    for k, g in itertools.groupby(s):
        g = list(g)
        if g[0] not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' and len(g) > length:
            start = current_index
            length = len(g)
            char = g[0]
        current_index += len(g)
    return [str(ord(char)), length, [start, start + length - 1]]