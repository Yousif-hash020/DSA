class Node:
    def __init__(self, info, next= None):
        self.info = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert_at_beginning(self, info):
        new_node = Node(info)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        current = self.head

        while current is not None:
            print(current.info, end=" --> ")
            current = current.next
        print("none")


linkdlist= SinglyLinkedList()

linkdlist.insert_at_beginning(10)
linkdlist.insert_at_beginning(9)
linkdlist.insert_at_beginning(8)
linkdlist.insert_at_beginning(7)
linkdlist.insert_at_beginning(6)

linkdlist.display()