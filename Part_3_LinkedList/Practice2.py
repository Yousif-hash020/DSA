class Node:
    def __init__(self, info, next=None, prev = None):
        self.info = info
        self.next = next
        self.prev = prev

class DbLinkedlist:
    def __init__(self, head= None):
        self.head = head

    def insert_at_End(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return   
        t1 = self.head

        while t1.next is not None:
            t1 = t1.next
        t1.next = new_node
        new_node.prev = t1
   
    def insert_at_start(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head.prev = new_node
        self.head= new_node
    
    def insertion_at_specific(self, target, value):

        new_node = Node(value)

        t1 = self.head

        while t1.next is not None:
            if  t1.info == target:
               break
            new_node.next = t1.next
            t1.next.prev = new_node
            t1.next = new_node
            new_node.prev = t1



    def display(self):
        t1 = self.head

        while t1 is not None:
            print(t1.info, end="<-->")
            t1 = t1.next
        print("None")


db = DbLinkedlist()

db.insert_at_End(20)
db.insert_at_End(20)
db.insert_at_End(20)
db.insert_at_End(20)
db.display()

db.insert_at_start(21)
db.insertion_at_specific(30,32)
        

db.display()

        
        