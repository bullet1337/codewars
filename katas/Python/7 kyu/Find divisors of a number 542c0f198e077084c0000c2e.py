# https://www.codewars.com/kata/542c0f198e077084c0000c2e
def divisors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)