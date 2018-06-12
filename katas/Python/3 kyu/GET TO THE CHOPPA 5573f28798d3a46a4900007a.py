# https://www.codewars.com/kata/5573f28798d3a46a4900007a
import collections


def find_shortest_path(grid, start_node, end_node):
    if not (grid and start_node and end_node):
        return []

    stack = collections.deque([start_node])
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[start_node.position.x][start_node.position.y] = True
    while stack:
        node = stack.pop()
        if node == end_node:
            path = [end_node]
            while path[-1] != start_node:
                path.append(visited[path[-1].position.x][path[-1].position.y])
            return path[::-1]

        for move in moves:
            x, y = node.position.x + move[0], node.position.y + move[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) \
                     and grid[x][y].passable and not visited[x][y]:
                visited[x][y] = node
                stack.appendleft(grid[x][y])