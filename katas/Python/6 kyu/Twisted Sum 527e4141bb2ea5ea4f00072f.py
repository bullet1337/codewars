# https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f
def compute_sum(n):
    return sum(int(d) for i in range(1, n + 1) for d in str(i))