# https://www.codewars.com/kata/514a024011ea4fb54200004b
import re


def domain_name(url):
    return re.search('(\/{2})?(w{3}.)?(?P<domain>[\w-]+)\.', url).group('domain')