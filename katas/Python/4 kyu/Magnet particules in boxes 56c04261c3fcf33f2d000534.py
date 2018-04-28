# https://www.codewars.com/kata/56c04261c3fcf33f2d000534
def doubles(maxk, maxn):
    return sum(1.0 / (k * ((n + 1.0)**(2 * k))) if k < 9 else 0 for n in range(1, maxn + 1) for k in range(1, maxk + 1))