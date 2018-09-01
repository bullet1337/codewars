# https://www.codewars.com/kata/58c5577d61aefcf3ff000081
def encode_rail_fence_cipher(string, n):
    if not string:
        return string

    def key(t):
        return abs((t[0] % (2 * n - 2)) - (n - 2))

    return string[0] + ''.join(t[1] for t in sorted(enumerate(string[1:]), key=key, reverse=True))
    
    
def decode_rail_fence_cipher(string, n):
    if not string:
        return string

    def key(t):
        return abs((t % (2 * n - 2)) - (n - 2))

    return string[0] + ''.join(t[1] for t in sorted(zip(sorted(range(len(string[1:])), key=key, reverse=True), string[1:]), key=lambda t: t[0]))