# https://www.codewars.com/kata/51fc3beb41ecc97ee20000c3
def make_looper(string):
    class Looper:
        def __init__(self):
            self.s = string
            self.i = -1
        
        def __call__(self):
            self.i += 1
            return self.s[self.i % len(self.s)]

    return Looper()