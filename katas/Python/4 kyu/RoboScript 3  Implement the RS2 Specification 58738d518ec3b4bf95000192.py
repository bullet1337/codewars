# https://www.codewars.com/kata/58738d518ec3b4bf95000192
import itertools
import re
from collections import defaultdict

direction_moves = {
    0: [0, 1],
    1: [1, 0],
    2: [0, -1],
    3: [-1, 0]
}


class Command:
    def __init__(self, ancestor):
        self.ancestor = ancestor
        self.count = 1

    def execute(self, grid, x=0, y=0, direction=0):
        pass


class SimpleCommand(Command):
    def __init__(self, ancestor, command):
        super().__init__(ancestor)
        self.command = command[0]
        self.count = len(command)

    def execute(self, grid, x=0, y=0, direction=0):
        if self.command == 'F':
            for _ in range(self.count):
                x += direction_moves[direction][0]
                y += direction_moves[direction][1]
                grid[x][y] = '*'
        else:
            if self.command == 'R':
                direction += self.count
            else:
                direction -= self.count
            direction %= 4
        return x, y, direction


class ComplexCommand(Command):
    def __init__(self, ancestor):
        super().__init__(ancestor)
        self.commands = []

    def execute(self, grid, x=0, y=0, direction=0):
        for _ in range(self.count):
            for command in self.commands:
                x, y, direction = command.execute(grid, x, y, direction)
        return x, y, direction


def execute(code):
    print(code)
    tokens = re.findall('(F+|R+|L+|\d+|[()])', code)
    current = ComplexCommand(None)
    for token in tokens:
        if token == '(':
            current = ComplexCommand(current)
            current.ancestor.commands.append(current)
        elif token == ')':
            current = current.ancestor
        elif token[0].isdigit():
            count = int(token)
            if count == 0 and isinstance(current.commands[-1], ComplexCommand):
                current.commands.pop()
            else:
                current.commands[-1].count += count - 1
                if current.commands[-1].count == 0:
                    current.commands.pop()
        else:
            if current.commands and isinstance(current.commands[-1], SimpleCommand) \
                    and token == current.commands[-1].command:
                current.commands[-1].count += 1
            else:
                current.commands.append(SimpleCommand(current, token))

    grid = defaultdict(lambda: defaultdict(lambda: ' '))
    grid[0][0] = '*'
    current.execute(grid)

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