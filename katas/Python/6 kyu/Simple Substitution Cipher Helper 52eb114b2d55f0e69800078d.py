# https://www.codewars.com/kata/52eb114b2d55f0e69800078d
from string import maketrans

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";


class Cipher(object):
    def __init__(self, map1, map2):
        self.tab = maketrans(map1, map2)
        self.itab = maketrans(map2, map1)
    
    def encode(self, string):
        return string.translate(self.tab)
    
    def decode(self, string):
        return string.translate(self.itab)