# https://www.codewars.com/kata/5583090cbe83f4fd8c000051
def digitize(n):
    return map(int, list(str(n)[::-1]))