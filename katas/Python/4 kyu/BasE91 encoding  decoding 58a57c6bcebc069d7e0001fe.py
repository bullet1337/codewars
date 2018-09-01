# https://www.codewars.com/kata/58a57c6bcebc069d7e0001fe
import struct

base91_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"')
decode_table = {l: i for i, l in enumerate(base91_alphabet)}


def b91decode(encoded_str):
    v = -1
    b = 0
    n = 0
    out = bytearray()
    for strletter in encoded_str:
        if not strletter in decode_table:
            continue
        c = decode_table[strletter]
        if v < 0:
            v = c
        else:
            v += c * 91
            b |= v << n
            n += 13 if v & 8191 > 88 else 14
            while True:
                out += struct.pack('B', b & 255)
                b >>= 8
                n -= 8
                if not n > 7:
                    break
            v = -1
    if v + 1:
        out += struct.pack('B', (b | v << n) & 255 )
    return out.decode('ascii') 


def b91encode(decode_str):
    bindata = decode_str.encode('ascii')
    ''' Encode a bytearray to a Base91 string '''
    b = 0
    n = 0
    out = ''
    for count in range(len(bindata)):
        byte = bindata[count:count+1]
        b |= struct.unpack('B', byte)[0] << n
        n += 8
        if n>13:
            v = b & 8191
            if v > 88:
                b >>= 13
                n -= 13
            else:
                v = b & 16383
                b >>= 14
                n -= 14
            out += base91_alphabet[v % 91] + base91_alphabet[v // 91]
    if n:
        out += base91_alphabet[b % 91]
        if n > 7 or b > 90:
            out += base91_alphabet[b // 91]
    return out