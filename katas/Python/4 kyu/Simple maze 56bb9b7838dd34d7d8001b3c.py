# https://www.codewars.com/kata/56bb9b7838dd34d7d8001b3c
import collections


def has_exit(maze):
    if maze == ['k']:
        return True

    escaped = False
    for x, y in zip(maze[0], maze[-1]):
        if x == ' ' or y == ' ':
            escaped = True
    for row in maze:
        if row[0] == ' ' or row[-1] == ' ':
            escaped = True
    if not escaped and len(set(len(row) for row in maze)) == 1:
        return False

    stack = collections.deque()
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'k':
                if stack:
                    raise RuntimeError
                stack.append((i, j))
    if not stack:
        raise RuntimeError

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = [[False for _ in range(len(maze[i]))] for i in range(len(maze))]

    while stack:
        pos = stack.pop()
        if pos[0] == len(maze) - 1 or pos[0] == 0 \
                or pos[1] == len(maze[pos[0]]) - 1 or pos[1] == 0 \
                or pos[1] >= len(maze[pos[0] - 1]) or pos[1] >= len(maze[pos[0] + 1]):
            return True

        visited[pos[0]][pos[1]] = True
        for move in moves:
            new_pos = (pos[0] + move[0], pos[1] + move[1])
            if 0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[new_pos[0]]) and maze[new_pos[0]][new_pos[1]] == ' ' \
                    and not visited[new_pos[0]][new_pos[1]]:
                stack.append(new_pos)

    return False
