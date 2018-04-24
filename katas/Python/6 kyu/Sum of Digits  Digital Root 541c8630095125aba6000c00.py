# https://www.codewars.com/kata/541c8630095125aba6000c00
def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(int(c) for c in str(n)))