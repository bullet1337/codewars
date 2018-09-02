# https://www.codewars.com/kata/58b57ae2724e3c63df000006
def parse_html_color(color):
    if color[0] != '#':
        color = PRESET_COLORS[color.lower()]
    if len(color) == 4:
        return {c: v for c, v in zip('rgb', (int(h * 2, 16) for h in color[1:]))}
    else:
        return {c: v for c, v in zip('rgb', (int(color[i:i + 2], 16) for i in range(1, len(color), 2)))}
