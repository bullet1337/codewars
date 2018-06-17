# https://www.codewars.com/kata/55733d3ef7c43f8b0700007c
def pattern(n):
    return '\n'.join(''.join(str(j) for j in range(n, i, -1)) for i in range(n))