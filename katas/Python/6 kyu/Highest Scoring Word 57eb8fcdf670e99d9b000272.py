# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
def high(x):
    return max(x.split(), key=lambda w: sum(ord(c) - ord('a') + 1 for c in w))