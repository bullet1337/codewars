# https://www.codewars.com/kata/52945ce49bb38560fe0001d9
def pascal(p):
    res = [[1]]
    for _ in range(p - 1):
        res.append(res[-1][:1] + [res[-1][i] + res[-1][i - 1] for i in range(1, len(res[-1]))] + res[-1][:1])
    return res