# https://www.codewars.com/kata/55cacc3039607536c6000081
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    
def insert_nth(head, index, data):
    if index < 0:
        raise IndexError()
    elif index == 0:
        return Node(data, head)
    
    node = head
    while index > 1 and node is not None:
        node = node.next
        index -= 1
    
    if node is None:
        raise IndexError()
    
    node.next = Node(data, node.next)
    return head