# https://www.codewars.com/kata/53fc954904a45eda6b00097f
from numbers import Number


class list(list):
    def __init__(self, arr):
        super(list, self).__init__(e for e in arr if isinstance(e, Number))

    def even(self):
        return [e for e in self if e % 2 == 0]
        
    def odd(self):
        return [e for e in self if e % 2 == 1]
    
    def under(self, v):
        return [e for e in self if e < v]
    
    def over(self, v):
        return [e for e in self if e > v]
    
    def in_range(self, f, t):
        return [e for e in self if f <= e <= t]