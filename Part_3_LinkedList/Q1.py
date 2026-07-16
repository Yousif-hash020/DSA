class Node:
    def __init__(self, info, next = None):
        self.info = info 
        self.next = next

class SinglyLinkedlist:
    def __init__(self, head=None):
        self.head = head
    
    def add_at_start(self, new_node):
        new_node = Node(new_node)
        new_node.next = self.head
        self.head = new_node
    
    def add_at_end(self, new_node):
        new_node = Node(new_node)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head

        while last.next is not None:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.info, end="-->")
            current = current.next
        print("None")

linklist = SinglyLinkedlist()

node1 = Node("perfect")
node2 = Node("behaviour")
node3 = Node("Faded")

node1.next = node2
node2.next = node3

linklist.head = node1

linklist.display()

linklist.add_at_start("Baby")
linklist.display()

linklist.add_at_end("My_Baby")
linklist.display()