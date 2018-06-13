# https://www.codewars.com/kata/5121303128ef4b495f000001
class Person:

    def __init__(self, name):
        self.name = name
        
    def greet(self, other_name):
        return 'Hello {}, my name is {}'.format(other_name, self.name)