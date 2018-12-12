# https://www.codewars.com/kata/5226eb40316b56c8d500030f
def pascals_triangle(n):
    result = [[1]]
    for _ in range(n - 1):
        result.append([1] + [result[-1][i] + result[-1][i + 1] for i in range(len(result[-1]) - 1)] + [1])
    return [e for r in result for e in r]