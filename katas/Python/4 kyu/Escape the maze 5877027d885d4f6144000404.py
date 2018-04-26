# https://www.codewars.com/kata/5877027d885d4f6144000404
import collections


def escape(maze):
    escaped = False
    for x, y in zip(maze[0], maze[-1]):
        if x == ' ' or y == ' ':
            escaped = True
    for row in maze:
        if row[0] == ' ' or row[-1] == ' ':
            escaped = True
    if not escaped:
        return []

    stack = collections.deque()
    for i in range(1, len(maze) - 1):
        for j in range(1, len(maze[i]) - 1):
            if maze[i][j] == '>':
                stack.append([i, j, 'R', ''])
            elif maze[i][j] == '<':
                stack.append([i, j, 'L', ''])
            elif maze[i][j] == '^':
                stack.append([i, j, 'U', ''])
            elif maze[i][j] == 'v':
                stack.append([i, j, 'D', ''])

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    moves_map = {
        moves[0]: 'R',
        moves[1]: 'D',
        moves[2]: 'L',
        moves[3]: 'U'
    }

    rotation_map = {
        moves[0]: {'L': 'B', 'R': '', 'U': 'R', 'D': 'L'},
        moves[2]: {'L': '', 'R': 'B', 'U': 'L', 'D': 'R'},
        moves[1]: {'L': 'L', 'R': 'R', 'U': 'B', 'D': ''},
        moves[3]: {'L': 'R', 'R': 'L', 'U': '', 'D': 'B'}
    }

    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    while stack:
        pos = stack.pop()
        if pos[0] == len(maze) - 1 or pos[0] == 0 or pos[1] == len(maze[0]) - 1 or pos[1] == 0:
            return list(pos[3])

        visited[pos[0]][pos[1]] = True
        for move in moves:
            new_pos = (pos[0] + move[0], pos[1] + move[1], moves_map[move], pos[3] + rotation_map[move][pos[2]] + 'F')
            if 0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0]) and maze[new_pos[0]][new_pos[1]] == ' ' \
                    and not visited[new_pos[0]][new_pos[1]]:
                stack.append(new_pos)

    return []