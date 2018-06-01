# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key= key.decode('utf-8')
        self.alphabet = alphabet.decode('utf-8')
        self.char_map = {l: i for i, l in enumerate(self.alphabet)}
    
    def encode(self, text):
        text = text.decode('utf-8')
        return ''.join(self.alphabet[(self.char_map[l] + self.char_map[self.key[i % len(self.key)]]) % len(self.alphabet)] 
                       if l in self.alphabet else l for i, l in enumerate(text)
        ).encode('utf-8')
        
    
    def decode(self, text):
        text = text.decode('utf-8')
        return ''.join(self.alphabet[(self.char_map[l] - self.char_map[self.key[i % len(self.key)]]) % len(self.alphabet)] 
                       if l in self.alphabet else l  for i, l in enumerate(text)
        ).encode('utf-8')
