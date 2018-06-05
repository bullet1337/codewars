# https://www.codewars.com/kata/54baad292c471514820000a3
def create_number_class(alphabet):
    class Generic:
    
        abc = alphabet
        base = len(abc)
        char_map = {c: i for i, c in enumerate(abc)}
        
        def __init__(self, str, dec=None):
            self.str = str
            self.dec = dec or sum(pow(self.base, i) * self.char_map[c] for i, c in enumerate(reversed(str)))
        
        def convert_to(self, target):
            result = ''
            input = self.dec
            while input > 0:
                input, mod = divmod(input, target.base)
                result += target.abc[mod]
            return target(result[::-1] or target.abc[0], self.dec)
        
        def __add__(self, other):
            return self.__class__('', self.dec + other.dec).convert_to(self.__class__)
        
        def __sub__(self, other):
            return self.__class__('', self.dec - other.dec).convert_to(self.__class__)
        
        def __mul__(self, other):
            return self.__class__('', self.dec * other.dec).convert_to(self.__class__)
        
        def __floordiv__(self, other):
            return self.__class__('', self.dec // other.dec).convert_to(self.__class__)
        
        def __str__(self):
            return self.str
    
    return Generic