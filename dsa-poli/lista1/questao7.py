class ReqImp:
    def __init__(self, numero, tamanho):
        self.numero = numero
        self.tamanho = tamanho
    
class CQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.start = 0
        self.end = 0
        self.actsize = 0

    def isFull(self):
        return self.actsize == self.size
    
    def isEmpty(self):
        return self.actsize == 0
    
    def enqueue(self, req):
        if self.isFull():
            return False
        
        self.queue [self.end] = req
        self.end = (self.end + 1) % (self.size)
        self.actsize += 1

        return True

    def dequeue(self):
        if self.isEmpty():
            return None
        
        actreq = self.queue[self.start]
        self.queue[self.start] = None
        

        self.start = (self.start + 1) % (self.size)
        self.actsize -= 1
        
        return actreq
    



