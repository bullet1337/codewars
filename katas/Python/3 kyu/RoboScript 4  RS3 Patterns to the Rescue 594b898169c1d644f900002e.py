# https://www.codewars.com/kata/594b898169c1d644f900002e
import itertools
import re
from collections import defaultdict

direction_moves = {
    0: [0, 1],
    1: [1, 0],
    2: [0, -1],
    3: [-1, 0]
}


class Instruction:
    def execute(self, grid, x=0, y=0, direction=0):
        pass


class Command(Instruction):
    def __init__(self):
        self.count = 1


class SimpleCommand(Command):
    def __init__(self, command):
        super().__init__()
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

    def __str__(self):
        return self.command + str(self.count)

    __repr__ = __str__


class ComplexCommand(Command):
    def __init__(self, ancestor=None):
        super().__init__()
        self.ancestor = ancestor
        self.commands = []

    def execute(self, grid, x=0, y=0, direction=0):
        for _ in range(self.count):
            for command in self.commands:
                x, y, direction = command.execute(grid, x, y, direction)
        return x, y, direction

    def __str__(self):
        return '{}: {}'.format(self.count, ' '.join(str(command) for command in (self.commands)))

    __repr__ = __str__


class FunctionCall(Instruction):
    def __init__(self, functions, id):
        self.functions = functions
        self.id = id

    def execute(self, grid, x=0, y=0, direction=0):
        if self.id not in self.functions:
            raise SyntaxError('{} function isn\'t defined'.format(self.id))
        else:
            return self.functions[self.id].execute(grid, x, y, direction)

    def __str__(self):
        return 'P' + str(self.id)

    __repr__ = __str__


def execute(code):
    tokens = re.findall('(F+|R+|L+|p|q|P|\d+|[()])', code)
    functions = {}
    functions_map = defaultdict(list)

    function = None
    function_id = None
    function_call = False
    current = ComplexCommand(None)
    for token in tokens:
        if token == '(':
            current = ComplexCommand(current)
            current.ancestor.commands.append(current)
        elif token == ')':
            current = current.ancestor
        elif token[0].isdigit():
            count = int(token)
            if function is not None and function_id is None:
                function_id = count
            elif function_call:
                if count == function_id:
                    raise SyntaxError('recursion detected in {} function'.format(function_id))
                elif function_id in functions_map[count]:
                    raise SyntaxError('mutual recursion detected in {}:{} functions'.format(function_id, count))

                functions_map[function_id].append(count)
                current.commands.append(FunctionCall(functions, count))
                function_call = False
            elif count == 0 and isinstance(current.commands[-1], ComplexCommand):
                current.commands.pop()
            else:
                current.commands[-1].count += count - 1
                if current.commands[-1].count == 0:
                    current.commands.pop()
        elif token == 'p':
            function = len(current.commands)
        elif token == 'q':
            if function_id in functions:
                raise SyntaxError('{} function is already defined'.format(function))
            else:
                functions[function_id] = ComplexCommand()
                functions[function_id].commands = current.commands[function:]
                current.commands = current.commands[:function]
            function = None
            function_id = None
        elif token == 'P':
            function_call = True
        else:
            if current.commands and isinstance(current.commands[-1], SimpleCommand) \
                    and token == current.commands[-1].command \
                    and (function is None or function != len(current.commands)):
                current.commands[-1].count += 1
            else:
                current.commands.append(SimpleCommand(token))

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