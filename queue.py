from collections import deque
class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, item):
        
        return self.data.append(item)
    
    def dequeue(self):
        return self.data.popleft()
    
    def peek(self):
        return print(self.data[0])

que1 = Queue()

que1.enqueue(8)
que1.enqueue(1)
que1.enqueue(2)
que1.enqueue(3)
que1.enqueue(4)

print(que1.data)


que1.dequeue()


print(que1.data)
que1.peek()
