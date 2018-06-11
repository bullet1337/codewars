# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991
def revrot(s, sz):
    return '' if not(0 < sz <= len(s)) else ''.join(s[i:i + sz][::-1] if sum(int(d) ** 3 for d in s[i:i+sz]) % 2 == 0 else s[i + 1:i + sz] + s[i] for i in range(0, len(s), sz) if i + sz < len(s))