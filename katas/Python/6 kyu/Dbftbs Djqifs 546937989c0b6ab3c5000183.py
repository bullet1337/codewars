# https://www.codewars.com/kata/546937989c0b6ab3c5000183
def encryptor(key, message):
    def encode(l):
        return chr(ord('A' if l.isupper() else 'a')  + (ord(l) - ord('A' if l.isupper() else 'a') + key) % 26)
    
    return ''.join(encode(l) if l.isalpha() else l for l in message)
