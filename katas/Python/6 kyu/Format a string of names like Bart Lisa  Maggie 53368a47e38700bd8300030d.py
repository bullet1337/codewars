# https://www.codewars.com/kata/53368a47e38700bd8300030d
def namelist(names):
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]['name']
    else:
        return '{} & {}'.format(', '.join(x['name'] for x in names[:-1]), names[-1]['name'])