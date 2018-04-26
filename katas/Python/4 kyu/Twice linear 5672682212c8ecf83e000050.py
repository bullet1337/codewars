# https://www.codewars.com/kata/5672682212c8ecf83e000050
from collections import deque


def dbl_linear(n):
    h = 1
    cnt = 0
    q2, q3 = deque(), deque()
    while cnt < n:
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0], q3[0])
        if h == q2[0]:
            h = q2.popleft()
        if h == q3[0]:
            h = q3.popleft()
        cnt += 1
    return h