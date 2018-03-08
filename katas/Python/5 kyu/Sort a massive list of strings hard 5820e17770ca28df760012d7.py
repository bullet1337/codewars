# https://www.codewars.com/kata/5820e17770ca28df760012d7
from heapq import heappush, heappop



def sort(words):
    h = []
    for value in words:
        heappush(h, value)
    return (heappop(h) for i in range(len(h)))