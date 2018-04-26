# https://www.codewars.com/kata/5765870e190b1472ec0022a2
moves = [
    lambda x, y: (x, y + 1),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x - 1, y),
]


def path_finder(maze):
    maze = maze.split('\n')
    stack = [(0, 0)]
    visited = set()

    while stack:
        pos = stack.pop()
        if pos[0] == len(maze) - 1 and pos[1] == len(maze) - 1:
            return True

        visited.add(pos)
        for move in moves:
            new_pos = move(*pos)
            if new_pos not in visited and \
                    0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze) and maze[new_pos[0]][new_pos[1]] == '.':
                stack.append(new_pos)

    return False