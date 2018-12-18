# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e
def int32_to_ip(int32):
    int32 = bin(int32)[2:].rjust(32, '0')
    return '.'.join(str(int(int32[i:i + 8], 2)) for i in range(0, 32, 8))