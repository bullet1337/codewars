# https://www.codewars.com/kata/55e67e44bf97fa66900000a0
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    

def sorted_intersect(first, second):  
    if first is None or second is None:
        return None
        
    head = current = None
    while first is not None and second is not None:    
        if first.data > second.data:
            first, second = second, first
            
        while first is not None and first.data < second.data:
            first = first.next
        if first is None:
            break
            
        if first.data == second.data:
            if current is None:
                head = current = first
            else:
                current.next = first
                current = current.next
            while first is not None and first.data == current.data:
                first = first.next
            while second is not None and second.data == current.data:
                second = second.next   
            
    if current is not None:
        current.next = None
    return head
