# https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5
def reverse_number(n):
    n = str(n)
    return int(n[::-1]) if n[0] != '-' else -int(n[:0:-1])