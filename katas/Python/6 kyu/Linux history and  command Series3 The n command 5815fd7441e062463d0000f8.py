# https://www.codewars.com/kata/5815fd7441e062463d0000f8
def bang_minus_n(n, history):
    try:
        return history.split('\n')[-n].split(maxsplit=1)[1]
    except:
        return '!-{}: event not found'.format(n)
 