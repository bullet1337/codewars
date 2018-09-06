# https://www.codewars.com/kata/55cc33e97259667a08000044
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sorted_insert(head, data):
    prev = None
    node = head
    while node is not None and node.data < data:
        prev = node
        node = node.next
        
    if prev is None:
        return Node(data, head)
    else:
        prev.next = Node(data, prev.next)
        return head