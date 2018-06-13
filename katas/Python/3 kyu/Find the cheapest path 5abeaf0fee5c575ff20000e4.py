# https://www.codewars.com/kata/5abeaf0fee5c575ff20000e4
from heapq import *


def cheapest_path(t, start, finish):   
    moves = [(0, 1, 'right'), (1, 0, 'down'), (0, -1, 'left'), (-1, 0, 'up')]
    stack = [(t[start[0]][start[1]], start[0], start[1])]
    heapify(stack)
    dist_map = [[(1e9, None, None) for _ in range(len(t[0]))] for _ in range(len(t))]
    dist_map[start[0]][start[1]] = (t[start[0]][start[1]], None, None)
    visited = [[False for _ in range(len(t[0]))] for _ in range(len(t))]
    while stack:
        z, x, y = heappop(stack)
        if visited[x][y]:
            continue

        visited[x][y] = True
        for move in moves:
            x_new, y_new = x + move[0], y + move[1]
            if 0 <= x_new < len(t) and 0 <= y_new < len(t[0]) and not visited[x_new][y_new] and dist_map[x_new][y_new][0] > z + t[x_new][y_new]:
                dist_map[x_new][y_new] = (z + t[x_new][y_new], (x, y), move[-1])
                heappush(stack, (dist_map[x_new][y_new][0], x_new, y_new))
    last = finish
    path = []
    while last != start:
        last = dist_map[last[0]][last[1]]
        path.append(last[-1])
        last = last[1]
    return path[::-1]
