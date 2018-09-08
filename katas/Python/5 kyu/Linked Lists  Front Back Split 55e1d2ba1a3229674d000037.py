# https://www.codewars.com/kata/55e1d2ba1a3229674d000037
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def front_back_split(source, front, back):
    if source is None or source.next is None:
        raise ValueError()
        
    front_last = None
    slow = fast = source
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        front_last = slow
        slow = slow.next
    
    if fast is not None:
        front_last = slow
        slow = slow.next
        
    back.data, back.next = slow.data, slow.next
    front_last.next = None
    front.data, front.next = source.data, source.next