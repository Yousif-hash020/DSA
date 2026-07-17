class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

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
        print(None)
        
ll = SinglyLinkedList()

ll.insert_at_end(10)
ll.insert_at_end(10)
ll.insert_at_end(10)
ll.insert_at_end(10)
ll.insert_at_end(10)
ll.insert_at_end(10)
ll.insert_at_end(10)

ll.display()

    
 

        
        