class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next
    
class DesignList:
    def __init__(self, head = None):
        self.head = head

    def insert_at_Start(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        t1 = self.head

        while t1.next is not None:
            t1 = t1.next
        t1.next = new_node

    def insert_at_specific(self,target, value):
        temp = Node(value)

        t1 = self.head 

        while t1.next is not None:
            if target == t1.info:
                temp.next = t1.next
                t1.next = temp 
            t1= t1.next
    def deleteLl(self, value):
        t1 = self.head
        prev = t1

        while t1.next is not None:
            if t1.info == value:
                prev.next = t1.next
            
            prev = t1 
            t1 = t1.next 

    def deletefirst(self):
        t1 = self.head 

        self.head = t1.next
    
    def dellast(self):
        t1 = self.head
        while t1.next.next is not None:
          t1= t1.next
        t1.next = None
          

    def display(self):
        t1 = self.head
        while t1 is not None:
            print(t1.info, end="-->") 
            t1 = t1.next
        print("none")

ll = DesignList()

ll.insert_at_last(20)
ll.insert_at_Start(5)
ll.insert_at_specific(5,8)
ll.insert_at_specific(8,10)
ll.insert_at_specific(10,40)
ll.deleteLl(10)
ll.deletefirst()

ll.dellast()

ll.display()
        

        

            