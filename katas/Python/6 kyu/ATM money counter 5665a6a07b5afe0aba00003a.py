# https://www.codewars.com/kata/5665a6a07b5afe0aba00003a
import re


def atm(value):
    currency = re.search('[a-z]+', value, re.IGNORECASE).group().upper()
    money = int(re.search('\d+', value).group())

    if currency not in VALUES:
        return 'Sorry, have no {}.'.format(currency)

    result = ''
    mod = money
    for value in sorted(VALUES[currency], reverse=True):
        div, mod = divmod(mod, value)
        if div > 0:
            result += '{} * {} {}'.format(div, value, currency)
            if mod == 0:
                break
            else:
                result += ', '
    if mod != 0:
        return 'Can\'t do {} {}. Value must be divisible by {}!'.format(money, currency, value)

    return result