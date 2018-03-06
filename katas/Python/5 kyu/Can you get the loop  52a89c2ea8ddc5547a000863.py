# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863
from collections import defaultdict


def loop_size(node):
    visited = defaultdict(int)
    i = 0
    while node not in visited:
        visited[node] = i
        i += 1
        node = node.next
    return i - visited[node]



