class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def pop(self):
        if self.is_empty():
            return len(self.data) == 0
        return self.data.pop() 
        
    def peek(self):
        if self.is_empty():
            return len(self.data) == 0
        
        return self.data[-1]
    
    def size(self):
        return len(self.data)
    
st1 = Stack()

st1.push(1)
st1.push(2)
st1.push(3)
st1.push(3)
st1.push(3)
st1.push(3)

print(st1.data)

print(st1.pop())
print(st1.peek())

print(st1.size())

