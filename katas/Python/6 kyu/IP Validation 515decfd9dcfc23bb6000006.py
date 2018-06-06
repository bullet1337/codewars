# https://www.codewars.com/kata/515decfd9dcfc23bb6000006
def is_valid_IP(strng):
    bytes = strng.split('.')
    return len(bytes) == 4 and all(byte.isdigit() and (len(byte) == 1 or byte[0] != '0') and 0 <= int(byte) <= 255 for byte in bytes)