# https://www.codewars.com/kata/529a92d9aba78c356b000353
from functools import reduce
import inspect


class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    
    @classmethod
    def from_array(cls, arr):
        print(arr)
        return reduce(lambda x, y: Cons(y, x), arr[::-1], None)
    
    def filter(self, fn):
        if not fn(self.head):
            return self.tail.filter(fn) if self.tail is not None else None
        else:
            return Cons(self.head, None if self.tail is None else self.tail.filter(fn))
    
    def map(self, fn):
        return Cons(fn(self.head), None if self.tail is None else self.tail.map(fn))
        
    def to_array(self):
        arr = []
        current = self
        while current is not None:
            arr.append(current.head)
            current = current.tail
        return arr