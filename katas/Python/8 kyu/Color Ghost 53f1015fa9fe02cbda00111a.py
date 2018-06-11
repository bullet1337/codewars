# https://www.codewars.com/kata/53f1015fa9fe02cbda00111a
class Ghost(object):
    colors = ['white', 'yellow', 'purple', 'red']
    i = 0

    def __init__(self):
        self.color = self.colors[Ghost.i % len(self.colors)]
        Ghost.i += 1
