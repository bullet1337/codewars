# https://www.codewars.com/kata/54a91a4883a7de5d7800009c
def increment_string(strng):
    print(strng)
    number = ''
    for i, c in enumerate(strng[::-1]):
        if not c.isdigit():
            break
        number += c
    return strng[:-i - (len(number) == len(strng))] + str(int(number[::-1]) + 1).rjust(len(number), '0') if number else strng + '1' 