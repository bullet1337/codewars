# https://www.codewars.com/kata/54fb963d3fe32351f2000102
def collatz(n):
    c = 1
    while n != 1:
        if n % 2:
            n = n * 3 + 1
        else:
            n /= 2
        c += 1
    return c