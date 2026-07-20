class Circular_Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity 
    
    def Enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size +=1
    def Deque(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        item =  self.queue[self.front] 
        self.queue[self.front] = None

        self.front = (self.front +1) % self.capacity
        self.size -= 1

        return item 
    
    def Front(self):
        if self.is_empty():
            print("queue is empty")
            return
        
        return self.queue[self.front]
    
    def Rear(self):
        if self.is_empty():
            print("queue is empty")
            return
        
        return self.queue[self.rear]

        
    def diaplay(self):
        print(self.queue)


    
cq = Circular_Queue(6)

cq.Enqueue(1)
cq.Enqueue(2)
cq.Enqueue(3)
cq.Enqueue(4)
  
cq.Deque()
cq.Deque()
cq.Deque()

cq.Enqueue(5)
cq.Enqueue(6)
cq.Enqueue(6)
cq.Enqueue(6)

cq.diaplay()
print(cq.Front())
print(cq.Rear())
