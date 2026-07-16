class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next

class SinglyLinklist:
    def __init__(self, head= None):
        self.head = head 
    
    def del_at_beg(self):
        if self.head is  None:
            print("Empty")
            return
        self.head = self.head.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.info, end="-->")
            current = current.next

        print("none")

linklist = SinglyLinklist()

node1 = Node(10)
node2 = Node(101)
node3 = Node(103)
node4 = Node(105)

        
node1.next = node2
node2.next = node3
node3.next = node4

linklist.head = node1

linklist.display()
        
linklist.del_at_beg()
linklist.display()        