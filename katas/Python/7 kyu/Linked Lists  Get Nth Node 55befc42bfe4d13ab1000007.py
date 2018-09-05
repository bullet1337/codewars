# https://www.codewars.com/kata/55befc42bfe4d13ab1000007
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
def get_nth(node, index):
    if index < 0:
        raise IndexError()
    
    while index > 0 and node is not None:
        node = node.next
        index -= 1
    
    if node is None:
        raise IndexError()
    return node
  