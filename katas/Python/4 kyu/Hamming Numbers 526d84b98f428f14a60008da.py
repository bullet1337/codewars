# https://www.codewars.com/kata/526d84b98f428f14a60008da
from heapq import heappop, heappush


def hamming(n):
    heap = []
    heappush(heap, 1)
    h = 0
    while n > 0:
        while heap[0] == h:
            heappop(heap)
        h = heappop(heap)
        heappush(heap, h * 2)
        heappush(heap, h * 3)
        heappush(heap, h * 5)
        n -= 1
    return h