# https://www.codewars.com/kata/54da539698b8a2ad76000228
from collections import Counter


def isValidWalk(walk):
    if len(walk) != 10:
        return False
    
    sides = Counter(walk)
    return sides['n'] == sides['s'] and sides['w'] == sides['e']