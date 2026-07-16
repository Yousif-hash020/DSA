class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next

class SiglyLinkedList:
    def __init__(self, head=None):
        self.head = head


node1 = Node(10)
node2 = Node(11)
node3 = Node(13)

node1.next = node2      
node2.next = node3      

LinkedList = SiglyLinkedList()

LinkedList.head = node1

current = LinkedList.head

while current is not  None:
    print(current.info, end=" --> ")
    current = current.next

print("None")