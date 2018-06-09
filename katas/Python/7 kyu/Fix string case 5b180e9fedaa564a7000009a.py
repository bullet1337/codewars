# https://www.codewars.com/kata/5b180e9fedaa564a7000009a
def solve(s):
    return s.lower() if sum(1 if c.islower() else -1 for c in s) >= 0 else s.upper()