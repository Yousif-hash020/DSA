from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def Enqueue(self, item ):
        return self.data.append(item)
    
    def checked_duplicate (self):
        checked =[]

        for item in self.data:
            if item not in checked:
                count = self.data.count(item)

                if count > 1:
                    print(item,"repeated", count, "times")
        
                checked.append(item)


         


        
    
    

q1 = Queue()

q1.Enqueue(1)
q1.Enqueue(1)
q1.Enqueue(2)
q1.Enqueue(2)

q1.checked_duplicate()

