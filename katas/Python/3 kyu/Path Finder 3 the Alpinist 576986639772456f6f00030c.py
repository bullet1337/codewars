# https://www.codewars.com/kata/576986639772456f6f00030c
from heapq import *


def path_finder(maze):
    maze = maze.split('\n')
    stack = [(0, 0, 0)]
    heapify(stack)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    dist_map = [[1e9 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    dist_map[0][0] = 0
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    while stack:
        z, x, y = heappop(stack)
        if visited[x][y]:
            continue

        visited[x][y] = True
        for move in moves:
            x_new, y_new = x + move[0], y + move[1]
            if 0 <= x_new < len(maze) and 0 <= y_new < len(maze[0]) and not visited[x_new][y_new]:
                dist_map[x_new][y_new] = min(dist_map[x_new][y_new], z + abs(ord(maze[x][y]) - ord(maze[x_new][y_new])))
                heappush(stack, (dist_map[x_new][y_new], x_new, y_new))
    return dist_map[len(maze) - 1][len(maze) - 1]