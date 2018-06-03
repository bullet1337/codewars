# https://www.codewars.com/kata/54c1bf903f0696f04600068b
import re
from functools import reduce
from operator import add, sub, mul, floordiv, and_, or_, xor


class Machine(object):
    
    def __init__(self, cpu):
        self.cpu = cpu
        self.op_map = {'add': add, 'sub': sub, 'mul': mul, 'div': floordiv, 'and': and_, 'or': or_, 'xor': xor}
    
    def execute(self, instr):
        cmd, *args = re.match('(\w+)(?: ([\w\d]+)(?:, ([\w\d]+))*)?', instr).groups()
        print(cmd, args)
        if cmd == 'push':
            self.cpu.write_stack(int(args[0]) if args[0].isdigit() else self.cpu.read_reg(args[0]))
        elif cmd == 'pop':
            if args[0] is None:
                self.cpu.pop_stack()
            else:
                self.cpu.write_reg(args[0], self.cpu.pop_stack())
        elif cmd == 'pushr':
            for r in 'abcd':
                self.cpu.write_stack(self.cpu.read_reg(r))
        elif cmd == 'pushrr':
            for r in 'dcba':
                self.cpu.write_stack(self.cpu.read_reg(r))
        elif cmd == 'popr':
            for r in 'dcba':
                self.cpu.write_reg(r, self.cpu.pop_stack())
        elif cmd == 'poprr':
            for r in 'abcd':
                self.cpu.write_reg(r, self.cpu.pop_stack())
        elif cmd == 'mov':
            self.cpu.write_reg(args[1], int(args[0]) if args[0].isdigit() else self.cpu.read_reg(args[0]))
        else:
            if cmd[-1] == 'a':
                self.cpu.write_stack(self.cpu.read_reg('a'))
            self.cpu.write_reg('a' if args[1] is None else args[1],
                               reduce(self.op_map[cmd[:len(cmd)-(cmd[-1] == 'a')]], 
                                      (self.cpu.pop_stack() for _ in range(int(args[0]) if args[0].isdigit() else self.cpu.read_reg(args[0])))
      
            ))
