# https://www.codewars.com/kata/52fea6fd158f0576b8000089
class Converter():
    @staticmethod
    def to_ascii(h):
        return ''.join(chr(int(h[i:i + 2], 16)) for i in range(0, len(h), 2))
        
    @staticmethod
    def to_hex(s):
        return ''.join(hex(ord(l))[-2:] for l in s)