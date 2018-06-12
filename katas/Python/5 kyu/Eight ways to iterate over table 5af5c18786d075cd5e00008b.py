# https://www.codewars.com/kata/5af5c18786d075cd5e00008b
DIRECTION_UP, DIRECTION_LEFT, DIRECTION_DOWN, DIRECTION_RIGHT = range(1,5)


class Table:
    def __init__(self, data):
        self.data = data
        
    def get_range(self, dir):
        if dir == DIRECTION_UP:
            return range(len(self.data) - 1, -1, -1)
        elif dir == DIRECTION_LEFT:
            return range(len(self.data[0]) - 1, -1, -1)
        elif dir == DIRECTION_DOWN:
            return range(len(self.data))
        elif dir == DIRECTION_RIGHT:
            return range(len(self.data[0]))
        
    def walk(self, dir0, dir1):
        for i in self.get_range(dir1):
            for j in self.get_range(dir0):                    
                yield self.data[j][i] if dir0 % 2 else self.data[i][j]
            
        
        
        
            