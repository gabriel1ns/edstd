class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.start = None


    def remover_duplicatas(self):
        current = self.start
        while current is not None:
            last_check = current
            check = current.next
            while check is not None:
                if check.data == current.data:
                    last_check.next = check.next
                else:
                    last_check = check

                check = last_check.next
            
            current = current.next


#resolucao n^2 pelo uso de nested loop
