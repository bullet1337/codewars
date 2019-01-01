# https://www.codewars.com/kata/5550d638a99ddb113e0000a2
def josephus(items, k):
    result = []
    i = 0
    while items:
        i = (i + k - 1) % len(items)
        result.append(items.pop(i))
    return result
        