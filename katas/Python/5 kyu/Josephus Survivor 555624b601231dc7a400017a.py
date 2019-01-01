# https://www.codewars.com/kata/555624b601231dc7a400017a
def josephus_survivor(n, k):
    i = 0
    items = list(range(1, n + 1))
    result = None
    while items:
        i = (i + k - 1) % len(items)
        result = items.pop(i)
    return result