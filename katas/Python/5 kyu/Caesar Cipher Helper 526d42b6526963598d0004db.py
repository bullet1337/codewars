# https://www.codewars.com/kata/526d42b6526963598d0004db
class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
    
    def cipher(self, text, mode):
        return ''.join(chr(ord('A') + (ord(l.upper()) - ord('A') + self.shift * (1 if mode else -1)) % 26) if l.isalpha() else l for l in text)
    
    def encode(self, text):
        return self.cipher(text, True)
        
    def decode(self, text):
        return self.cipher(text, False)