# https://www.codewars.com/kata/57eae65a4321032ce000002d
def fake_bin(x):
    return ''.join('0' if d < '5' else '1' for d in x)