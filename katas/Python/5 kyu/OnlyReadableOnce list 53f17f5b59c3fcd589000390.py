# https://www.codewars.com/kata/53f17f5b59c3fcd589000390
class SecureList():
    def __init__(self, l):
        self.l = list(l)
  
    def __str__(self):
        result = self.l
        self.l = []
        return str(result)
        
    __repr__ = __str__
    
    def __getitem__(self, item):
        result = self.l[item]
        del self.l[item]
        return result
        
    def __len__(self):
        return len(self.l)