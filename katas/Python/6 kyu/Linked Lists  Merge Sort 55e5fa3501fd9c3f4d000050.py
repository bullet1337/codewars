# https://www.codewars.com/kata/55e5fa3501fd9c3f4d000050
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
    

def front_back_split(source):
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
        
    front_last.next = None
    return source, slow


def merge_sort(list):
    if list is None or list.next is None:
        return list
    
    return sorted_merge(*(merge_sort(l) for l in front_back_split(list)))