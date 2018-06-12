# https://www.codewars.com/kata/57658bfa28ed87ecfa00058a
import collections


def path_finder(maze):
    maze = maze.split('\n')
    stack = collections.deque([(0, 0, 0)])
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited[0][0] = True
    while stack:
        pos = stack.pop()
        if pos[0] == len(maze) - 1 and pos[1] == len(maze[0]) - 1:
            return pos[2]

        for move in moves:
            new_pos = (pos[0] + move[0], pos[1] + move[1], pos[2] + 1)
            if 0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0]) \
                     and maze[new_pos[0]][new_pos[1]] == '.' and not visited[new_pos[0]][new_pos[1]]:
                visited[new_pos[0]][new_pos[1]] = True
                stack.appendleft(new_pos)
    return False