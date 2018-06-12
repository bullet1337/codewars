# https://www.codewars.com/kata/52ea928a1ef5cfec800003ee
def ip_to_int32(ip):
    return int(''.join(bin(int(byte))[2:].rjust(8, '0') for byte in ip.split('.')), 2)