# https://www.codewars.com/kata/55dd5386575839a74f0000a9
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError()

    first, second = head, head.next
    lists = [first, second]
    head = head.next.next
    i = 0
    while head is not None:
        lists[i % 2].next = head
        lists[i % 2] = lists[i % 2].next
        head = head.next
        i += 1
        
    for list in lists:
        list.next = None
    return Context(first, second)