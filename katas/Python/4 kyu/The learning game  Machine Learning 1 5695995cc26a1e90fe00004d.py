# https://www.codewars.com/kata/5695995cc26a1e90fe00004d
from collections import defaultdict

ACTIONS = [lambda x:x+1, lambda x:0, lambda x: x/2, lambda x: x*100, lambda x: x%2]


class Machine:

    def __init__(self):
        self.cmds = defaultdict(lambda: [list(range(5)), 0])
        self.cmd_answer = {}
        self.learned = {}

    def command(self, cmd, num):
        if cmd in self.learned:
            return self.learned[cmd](num)
    
        response = ACTIONS[self.cmds[cmd][1]](num)
        self.cmd_answer[cmd] = (num, response)
        self.last_cmd = cmd
        return response
        
    def response(self, res):
        if res:
            self.cmds[self.last_cmd][0] = [i for i in self.cmds[self.last_cmd][0] if self.cmd_answer[self.last_cmd][1] == ACTIONS[i](self.cmd_answer[self.last_cmd][0])]
            if len(self.cmds[self.last_cmd]) == 1:
                self.learned[cmd] == ACTIONS[self.cmds[0]]
        else:
            self.cmds[self.last_cmd][1] += 1