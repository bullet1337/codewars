# https://www.codewars.com/kata/54129112fb7c188740000162
def prefill(n, v='undefined'):
    if n is None:
        raise TypeError('{} is invalid'.format(n))
    if not isinstance(n, int):
        try:
            n = int(n)
        except ValueError:
            raise TypeError('{} is invalid'.format(n))
    if n < 0:
        raise TypeError('{} is invalid'.format(n))
    return [v] * n