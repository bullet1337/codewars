# https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2
def validate(n):
    return (sum(sum(int(d) for d in str(2 * (ord(c) - ord('0')))) for c in str(n)[len(str(n)) % 2::2])
            + sum(ord(c) - ord('0') for c in str(n)[(len(str(n)) + 1) % 2::2])) % 10 == 0