# https://www.codewars.com/kata/5862fb364f7ab46270000078
def encrypt(text, rule):
    return ''.join(chr((ord(l) + rule) % 256) for l in text)