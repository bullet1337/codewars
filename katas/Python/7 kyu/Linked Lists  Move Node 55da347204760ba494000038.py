# https://www.codewars.com/kata/55da347204760ba494000038
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
    
def move_node(source, dest):
    if source is None:
        raise ValueError()
    
    new_source = source.next
    source.next = dest
    return Context(new_source, source)