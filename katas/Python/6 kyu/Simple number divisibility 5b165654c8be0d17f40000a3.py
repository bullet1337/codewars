# https://www.codewars.com/kata/5b165654c8be0d17f40000a3
def solve(n):
    n = str(n)
    i0, i27, i5 = n.rfind('0'), max(n.rfind('2'), n.rfind('7')), n.rfind('5')
    i00 = n.rfind('0', 0, i0)
    dist = len(n) * 2
    if i00 != -1:
        local = len(n) - 1 - i0 + len(n) - 2 - i00
        dist = min(dist, local)
    if i5 != -1 and i0 != -1:
        i = 0
        if i5 == 0 and n[1] == '0' and len(n) > 2:
            i = 2
            while i < len(n) and n[i] == '0':
                i += 1
        if i < len(n):
            local = len(n) - 1 - i0 + len(n) - 2 - i5 + int(i0 < i5)
            if i > 0:
                local += i - 1 - int(i0 < i)
            dist = min(dist, local)
    if i27 != -1 and i5 != -1:
        i = 0
        if i5 == 0 or i27 == 0:
            if (i5 == 1 or i27 == 1) and len(n) > 2 and n[2] == '0':
                i = 3
            elif i5 != 1 and i27 != 1 and n[1] == '0':
                i = 2
            if i > 0:
                while i < len(n) and (n[i] == '0' or i == i5 or i == i27):
                    i += 1
        if i < len(n):
            local = len(n) - 1 - i5 + len(n) - 2 - i27 + int(i5 < i27)
            if i > 0:
                local += i - 1 - int(max(i5, i27) < i)
            dist = min(dist, local)
    
    return -1 if dist == len(n) * 2 else dist