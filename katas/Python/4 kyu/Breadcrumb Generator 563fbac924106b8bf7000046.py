# https://www.codewars.com/kata/563fbac924106b8bf7000046
import re

stop_words = {'the', 'of', 'in', 'from', 'by', 'with', 'and', 'or', 'for', 'to', 'at', 'a'}


def generate_bc(url, separator):
    matches = re.findall('(?<!\/)\/(?!index)([\w-]+)', url)
    last = '/'
    links = ['<a href="/">HOME</a>']
    if matches:
        for match in matches[:-1]:
            text = ''.join(x[0] for x in match.split('-') if x.lower() not in stop_words) if len(match) > 30 else match.replace('-', ' ')
            links.append('<a href="{}{}/">{}</a>'.format(last, match, text.upper()))
            last += match + '/'
        match = matches[-1]
        match = ''.join(x[0] for x in match.split('-') if x.lower() not in stop_words) if len(match) > 30 else match
        links.append('<span class="active">{}</span>'.format(match.replace('-', ' ').upper()))
    else:
        return '<span class="active">HOME</span>'
    return separator.join(links)