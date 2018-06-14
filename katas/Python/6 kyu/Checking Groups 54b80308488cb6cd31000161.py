# https://www.codewars.com/kata/54b80308488cb6cd31000161
def group_check(s):
    balances = [[0, 0, 0]]
    for c in s:
        i = '({['.find(c)
        if i != -1:
            balances[-1][i] += 1
            balances.append([0, 0, 0])
        else:
            if any(x != 0 for x in balances[-1]):
                return False
            balances.pop()
            if not balances:
                return False
            balances[-1][')}]'.find(c)] -=1
    return len(balances) == 1 and all(x == 0 for x in balances[-1])