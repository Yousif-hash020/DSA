class Node:
    def __init__(self, info,prev=None,next=None):
        self.info = info
        self.next = next
       

class ReverseLinkedList():
    def __init__(self, head=None):
        self.head = head
    
    def Reverse(self, prev=None ):

        self.prev = prev

        t1 = self.head
        while t1 is not None:
          next_node = t1.next
          t1.next = prev
          prev = t1
          t1 = next_node
        self.head = prev
  

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        t1 = self.head

        while t1.next is not None:
            t1 = t1.next

        t1.next = new_node

    def display(self):
        t1 = self.head

        while t1 is not None:
            print(t1.info, end="-->") 
            t1 = t1.next   
        print("none")


rl = ReverseLinkedList()

rl.insert_at_end(1)
rl.insert_at_end(2)
rl.insert_at_end(3)
rl.insert_at_end(4)

rl.Reverse()

rl.display()