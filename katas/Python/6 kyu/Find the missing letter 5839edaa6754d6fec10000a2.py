# https://www.codewars.com/kata/5839edaa6754d6fec10000a2
def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i]) != ord(chars[i + 1]) - 1:
            return chr(ord(chars[i]) + 1)
