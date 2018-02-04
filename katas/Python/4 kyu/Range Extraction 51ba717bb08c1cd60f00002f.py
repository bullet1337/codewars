# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
def solution(args):
    if not args:
        return ''

    result = ''
    start = args[0]
    end = args[0]
    for elem in args[1:] + ['']:
        if elem != end + 1:
            if end - start + 1 >= 3:
                result += '{}-{},'.format(start, end)
            else:
                if start != end:
                    result += '{},{},'.format(start, end)
                else:
                    result += '{},'.format(end)
            start = elem
        end = elem
    return result[:-1]