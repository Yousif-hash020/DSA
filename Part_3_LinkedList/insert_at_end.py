class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class SinglyLinklist:
    def __init__(self, head= None):
        self.head = head
    
    def push(self, new_node):
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
            print(current.info, end="--> ")
            current = current.next
        print("None")


linklist = SinglyLinklist()

linklist.push(20)
linklist.push(120)
linklist.push(320)
linklist.push(420)


linklist.display()
    
        