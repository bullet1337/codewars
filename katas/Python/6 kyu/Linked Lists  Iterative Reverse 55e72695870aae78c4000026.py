# https://www.codewars.com/kata/55e72695870aae78c4000026
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    
def reverse(head):
    if head is None:
        return None

    orig_head = head
    prev = Node(head.data)
    head = head.next
    while head is not None:
        head.next, prev, head, = prev, head, head.next
    orig_head.data, orig_head.next = prev.data, prev.next