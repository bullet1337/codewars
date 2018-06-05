# https://www.codewars.com/kata/5a12755832b8b956a9000133
import re
from itertools import chain
from collections import defaultdict


recursion_limit = 500


class Instruction:
    def convert_to_raw(self):
        pass

class SimpleCommand(Instruction):
    def __init__(self, command, count=1):
        self.command = command[0]
        self.count = count

    def convert_to_raw(self, depth=None):
        return [self.command] * self.count

    def __str__(self):
        return self.command + str(self.count)


class ComplexCommand(Instruction):
    def __init__(self, ancestor=None, count=1):
        self.ancestor = ancestor
        self.commands = []
        self.count = count

    def convert_to_raw(self, depth=None):
        return list(chain(*(command.convert_to_raw() for command in self.commands))) * self.count

    def __str__(self):
        return '{}: {}'.format(self.count, ' '.join(str(command) for command in (self.commands)))


class FunctionCall(Instruction):
    def __init__(self, scope, id):
        self.scope = scope
        self.id = id
        self.raw = None
        
    def convert_to_raw(self, depth=0):
        if depth > recursion_limit:
            raise RuntimeError('Exceeded recursion depth')
    
        if self.raw is not None:
            return self.raw
    
        scope = self.scope
        while scope is not None and self.id not in scope.scopes:
            scope = scope.ancestor
            
        if scope is None:
            raise SyntaxError('Attempting to invoke a non-existent {} function'.format(self.id))
        elif scope == self.scope.ancestor and self.id == self.scope.id:
            raise SyntaxError('Recursion detected in {} function'.format(self.id))
      
        self.raw = list(chain(*(command.convert_to_raw(depth + 1) for command in scope.scopes[self.id].commands)))
        return self.raw

    def __str__(self):
        return 'P' + self.id


class Scope:
    def __init__(self, ancestor=None, id=None):
        self.ancestor = ancestor
        self.id = id
        self.commands = None
        self.scopes = {}
        

class RSUProgram:

    pattern = '[FRL)](?:0|[1-9]\d*)?|p(?:0|[1-9]\d*)|q|P(?:0|[1-9]\d*)|\(|(\/\/.*$|\/\*(?:.|[\r\n])*\*\/|\s+)'
    direction_moves = {
        0: [0, 1],
        1: [1, 0],
        2: [0, -1],
        3: [-1, 0]
    }

    def __init__(self, source):
        self.source = source
        
    def get_tokens(self):
        matches = re.finditer(self.pattern, self.source, re.MULTILINE)
        last = 0
        tokens = []
        for match in matches:
            if match.start() != last:
                raise SyntexError('Invalid token: {}'.format(self.source[last: match.start()]))
            
            if match.group(1) is None:
                tokens.append(match.group())
            last = match.end()
        if last != len(self.source):
            raise SyntexError('Invalid token: {}'.format(self.source[last:]))
        return tokens
        
    def convert_to_raw(self, tokens):
        brackets = 0
        scope = Scope()
    
        function = []
        function_id = []
        current = ComplexCommand(None)
        for token in tokens:
            if token[0] == '(':
                current = ComplexCommand(current)
                current.ancestor.commands.append(current)
                brackets += 1
            elif token[0] == ')':
                if len(token) > 1:
                    current.count = int(token[1:])
                current = current.ancestor
                if current.commands[-1].count == 0:
                    current.commands.pop()
                brackets -= 1
            elif token[0] == 'p':
                if brackets % 2 == 1:
                    raise SyntaxError('Nesting pattern definitions within bracketed sequences are not allowed')
                
                function_id.append(token[1:])
                if function_id[-1] in scope.scopes:
                    raise SyntaxError('Pattern redefinition in the same scope is not allowed')
                
                function.append(len(current.commands))
                scope = Scope(scope, function_id[-1])
                scope.ancestor.scopes[function_id[-1]] = scope
            elif token[0] == 'q':
                if brackets % 2 == 1:
                    raise SyntaxError('Brackets don\' match')
            
                scope.commands = current.commands[function[-1]:]
                current.commands = current.commands[:function[-1]]
                function.pop()
                function_id.pop()
                scope = scope.ancestor
            elif token[0] == 'P':
                current.commands.append(FunctionCall(scope, token[1:]))
            else:
                command, count = token[0], 1 if len(token) == 1 else int(token[1:])
                if count != 0:
                    if current.commands and isinstance(current.commands[-1], SimpleCommand) \
                            and command == current.commands[-1].command \
                            and (function is None or function != len(current.commands)):
                        current.commands[-1].count += count
                    else:
                        current.commands.append(SimpleCommand(token, count))
                        
        if brackets != 0:
            raise SyntaxError('Brackets don\' match')
        return current.convert_to_raw()
                
    def execute_raw(self, cmds):
        grid = defaultdict(lambda: defaultdict(lambda: ' '))
        grid[0][0] = '*'
        x = y = direction = 0
        for cmd in cmds:
            if cmd == 'F':
                x += self.direction_moves[direction][0]
                y += self.direction_moves[direction][1]
                grid[x][y] = '*'
            else:
                if cmd == 'R':
                    direction += 1
                else:
                    direction -= 1
                direction %= 4
    
        sorted_x = sorted(grid.keys())
        x_min = sorted_x[0]
        x_max = sorted_x[-1]
    
        sorted_y = sorted(chain(*grid.values()))
        y_min = sorted_y[0]
        y_max = sorted_y[-1]
    
        result = ''
        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                result += grid[i][j]
            result += '\r\n'
        return result[:-2]
        
    def execute(self):
        return self.execute_raw(self.convert_to_raw(self.get_tokens()))