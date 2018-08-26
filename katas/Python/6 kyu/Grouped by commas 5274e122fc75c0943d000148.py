# https://www.codewars.com/kata/5274e122fc75c0943d000148
def group_by_commas(n):
    n = str(n)
    return ','.join(reversed([n[max(i - 3, 0):i] for i in range(len(n), 0, -3)]))