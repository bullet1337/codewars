# https://www.codewars.com/kata/5268acac0d3f019add000203
from functools import reduce


class Automaton(object):

    def __init__(self):
        self.states = {
            'q1': {
                '0': 'q1',
                '1': 'q2'
            },
            'q2': {
                '0': 'q3',
                '1': 'q2'
            },
            'q3': {
                '0': 'q2',
                '1': 'q2'
            }
        }

    def read_commands(self, commands):
        return reduce(lambda x, y: self.states[x][y], commands, 'q1') == 'q2'


my_automaton = Automaton()