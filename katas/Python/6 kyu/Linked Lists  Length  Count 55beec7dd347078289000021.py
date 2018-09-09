# https://www.codewars.com/kata/55beec7dd347078289000021
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
def length(node):
    length = 0
    while node is not None:
        length += 1
        node = node.next
    return length
  
  
def count(node, data):
    count = 0
    while node is not None:
        if node.data == data:
            count += 1
        node = node.next
    return count