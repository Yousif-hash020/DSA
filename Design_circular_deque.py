class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
         return -1
    
    def isFull(self):
        if self.size == self.k:
           return -1
        
    def insertLast(self, value):
      if self.isFull():
        return False

      self.rear = (self.rear + 1) % self.k
      self.queue[self.rear] = value
      self.size += 1



    def insertFront(self, value):
        
        if self.isFull():
         return False
                
        self.front = (self.front - 1 + self.k) % self.k
        self.queue[self.front] = value
        self.size += 1

        return True
    
    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def deleteFront(self):
        if self.isEmpty():
           return-1
        value = self.queue[self.rear] 
        self.queue[self.rear] = None

        self.front = (self.rear - 1 + self.k) % self.k
        self.size -= 1  
        return value
   
    def deleteLast(self):
        if self.isEmpty():
           return-1
        value = self.queue[self.front] 
        self.queue[self.front] = None

        self.front = (self.front +1) % self.k
        self.size -= 1  
        return value
    

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
   
    
    def Display(self):
       print(self.queue)
        

dcq = CircularQueue(8)



dcq.insertFront(1)
dcq.insertFront(2)
dcq.insertFront(3)


dcq.insertLast(4)
dcq.insertLast(5)
dcq.insertLast(6)
dcq.insertLast(7)
dcq.insertLast(8)

print(dcq.Front())
print(dcq.Rear())

dcq.Display()