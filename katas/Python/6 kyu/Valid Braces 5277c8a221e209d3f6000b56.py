# https://www.codewars.com/kata/5277c8a221e209d3f6000b56
close_braces = {')': '(', '}': '{', ']': '['}
open_braces = {'(', '{', '['}


def validBraces(string):
    balance = {'(': 0, '{': 0, '[': 0}
    for c in string:
        if c in open_braces:
            balance[c] += 1
        elif c in close_braces:
            balance[close_braces[c]] -= 1
            if balance[close_braces[c]] < 0:
                return False
    return all(x == 0 for x in balance.values())