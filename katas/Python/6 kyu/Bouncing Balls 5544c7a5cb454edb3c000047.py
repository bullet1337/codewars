# https://www.codewars.com/kata/5544c7a5cb454edb3c000047
from itertools import accumulate, repeat, takewhile


def bouncingBall(h, bounce, window):
    if not(h > 0 and 0 < bounce < 1 and window < h):
        return -1
    
    return len(list(takewhile(lambda x: x >= window, accumulate(repeat(h), lambda x, y: x * bounce)))) * 2 - 1