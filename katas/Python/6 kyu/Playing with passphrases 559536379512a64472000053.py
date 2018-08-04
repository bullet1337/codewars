# https://www.codewars.com/kata/559536379512a64472000053
def play_pass(s, n):
    return ''.join(chr(ord('0') + ord('9') - ord(c)) if c.isdigit() else 
                  (lambda x: x.upper() if i % 2 == 0 else x.lower())(
                      chr(ord('a' if c.islower() else 'A') + (ord(c) - ord('a' if c.islower() else 'A') + n) % 26)
                  ) if c.isalpha() 
                  else c for i, c in enumerate(s))[::-1]
    