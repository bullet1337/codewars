# https://www.codewars.com/kata/5870fa11aa0428da750000da
import itertools
from collections import defaultdict


direction_moves = {
    0: [0, 1],
    1: [1, 0],
    2: [0, -1],
    3: [-1, 0]
}


def execute(code):
    print(code)
    grid = defaultdict(lambda: defaultdict(lambda: ' '))
    x = y = 0
    grid[x][y] = '*'

    cmd = None
    count_str = ''
    count = 0
    direction = 0
    for c in code:
        if c.isdigit():
            count_str += c
        elif c == cmd:
            if count_str:
                count += int(count_str) - 1
            count_str = ''
            count += 1
        elif cmd is None:
            cmd = c
            count = 1
        else:
            if count_str:
                count += int(count_str) - 1

            if cmd == 'F':
                for _ in range(count):
                    x += direction_moves[direction][0]
                    y += direction_moves[direction][1]
                    grid[x][y] = '*'
            else:
                if cmd == 'R':
                    direction += count
                else:
                    direction -= count
                direction %= 4
            cmd = c
            count = 1
            count_str = ''
    if cmd == 'F':
        if count_str:
            count += int(count_str) - 1
        for _ in range(count):
            x += direction_moves[direction][0]
            y += direction_moves[direction][1]
            grid[x][y] = '*'

    sorted_x = sorted(grid.keys())
    x_min = sorted_x[0]
    x_max = sorted_x[-1]

    sorted_y = sorted(itertools.chain(*grid.values()))
    y_min = sorted_y[0]
    y_max = sorted_y[-1]

    result = ''
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            result += grid[i][j]
        result += '\r\n'
    return result[:-2]