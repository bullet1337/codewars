# https://www.codewars.com/kata/555eded1ad94b00403000071
def series_sum(n):
    return '{:0.2f}'.format(sum(1 / (i * 3 + 1) for i in range(0, n)))