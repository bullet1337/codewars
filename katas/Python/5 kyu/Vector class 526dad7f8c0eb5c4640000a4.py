# https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4
class Vector:

    def __init__(self, points):
        self.points = list(points)
    
    def add(self, other):
        if len(self.points) != len(other.points):
            raise Exception
        return Vector(x + y for x, y in zip(self.points, other.points))
        
    def subtract(self, other):   
        if len(self.points) != len(other.points):
            raise Exception 
        return Vector(x - y for x, y in zip(self.points, other.points))
        
    def dot(self, other):   
        if len(self.points) != len(other.points):
            raise Exception 
        return sum(x * y for x, y in zip(self.points, other.points))
        
    def norm(self):
        return sum(x * x for x in self.points) ** .5
        
    def __str__(self):
        return '({})'.format(','.join(str(x) for x in self.points))
        
    def equals(self, other):  
        if len(self.points) != len(other.points):
            return False
        return all(x == y for x, y in zip(self.points, other.points))
        
