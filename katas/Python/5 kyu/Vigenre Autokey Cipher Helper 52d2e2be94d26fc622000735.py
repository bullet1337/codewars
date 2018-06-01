# https://www.codewars.com/kata/52d2e2be94d26fc622000735
class VigenereAutokeyCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.char_map = {l: i for i, l in enumerate(self.alphabet)}
    
    def cipher(self, text, mode):
        output = ''
        key = self.key
        i = 0
        for l in text:
            if l in self.char_map:
                output += self.alphabet[(self.char_map[l] + self.char_map[key[i]] * (1 if mode else -1)) % len(self.alphabet)]
                key += l if mode else output[-1]
                i += 1
            else:
                output += l
        return output
    
    def encode(self, text):
        return self.cipher(text, True)
        
    def decode(self, text):
        return self.cipher(text, False)