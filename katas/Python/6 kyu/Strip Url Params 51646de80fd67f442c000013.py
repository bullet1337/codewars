# https://www.codewars.com/kata/51646de80fd67f442c000013
from collections import OrderedDict


def strip_url_params(url, params_to_strip = []):
    if '?' not in url:
        return url

    site, params = url.split('?')
    map = OrderedDict()
    for pair in params.split('&'):
        key, value = pair.split('=')
        if key not in map and key not in params_to_strip:
            map[key] = value
    
    return site + '?' + '&'.join(k + '=' + v for k, v in map.items())