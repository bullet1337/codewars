# https://www.codewars.com/kata/50654ddff44f800200000007
def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b
