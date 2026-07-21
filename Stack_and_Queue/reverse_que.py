from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()
    
    def Enque(self, item ):
        return self.data.append(item)
    
    def Reverse_que(self):

        stack = []

        while self.data:
            item = self.data.popleft()
            stack.append(item)
        
        print(stack)

        return stack
    
    def new_que(self, stack):
        while stack:
            item = stack.pop()
            self.data.append(item)
    
    def dispaly(self):
        print(self.data)


        
    

q1 = Queue()

q1.Enque(1)
q1.Enque(2)
q1.Enque(3)
q1.Enque(4)

stack =q1.Reverse_que()
q1.new_que(stack)
q1.dispaly()



