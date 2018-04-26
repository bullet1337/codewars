# https://www.codewars.com/kata/584dee06fe9c9aef810001e8
cache = [1, 5, 6]
i = 10
j = 10


def green(n):
    global i, j
    if n <= len(cache):
        return cache[n - 1]

    n -= len(cache)
    A = cache[-2]
    B = cache[-1]
    if A % 10 != 5:
        A, B = B, A

    while n > -1:
        both = 0

        i *= 10
        temp = A ** 2 % i
        if temp != A:
            A = temp
            cache.append(A)
            both += 1
            n -= 1

        new_j = j * 10
        temp = B + ((10 - B ** 2 % new_j // j) % 10) * j
        j = new_j
        if temp != B:
            B = temp
            cache.append(B)
            both += 1
            n -= 1

        if both == 2 and cache[-2] > cache[-1]:
            cache[-2], cache[-1] = cache[-1], cache[-2]
    return cache[-1 + n]