# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88
class CallableInt(int):
    
    def __call__(self, arg):
        return CallableInt(self + arg)


def add(number):
    return CallableInt(number)