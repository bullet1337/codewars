# https://www.codewars.com/kata/54557d61126a00423b000a45
def shorter_reverse_longer(a,b):
    if len(a) >= len(b):
        a, b = b, a
    return a + b[::-1] + a