# https://www.codewars.com/kata/5572f7c346eb58ae9c000047
def pattern(n):
    return '\n'.join(str(i) * i for i in range(1, n + 1))