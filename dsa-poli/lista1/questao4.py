class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.start = None
    
def mesclar(l1, l2):
    temp_start = Node(0)
    pointer_newl = temp_start

    pl1 = l1.start
    pl2 = l2.start

    while pl1 is not None and pl2 is not None:
        if pl1.data < pl2.data:
            pointer_newl.next = pl1
            pl1 = pl1.next
        else:
            pointer_newl.next = pl2
            pl2 = pl2.next
        pointer_newl = pointer_newl.next

    if pl1 is not None:
        pointer_newl.next = pl1
    elif pl2 is not None:
        pointer_newl.next = pl2
        
    newl = LL()
    newl.start = temp_start.next
    return newl
