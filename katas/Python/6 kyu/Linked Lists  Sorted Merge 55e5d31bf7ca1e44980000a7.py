# https://www.codewars.com/kata/55e5d31bf7ca1e44980000a7
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    
def sorted_merge(first, second):
    if first is None or second is None:
        return first or second
    
    head = current = first if first.data < second.data else second
    if first.data < second.data:
        first = first.next
    else:
        second = second.next
        
    while first is not None and second is not None:
        if first.data < second.data:
            current.next = first
            first = first.next
        else:
            current.next = second
            second = second.next
        current = current.next
    current.next = first or second
    return head