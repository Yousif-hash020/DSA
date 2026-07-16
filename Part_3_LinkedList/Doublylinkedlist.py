class Node:
    def __init__(self, info):
        self.info = info
        self.prev = None
        self.next = None

class DoublyLinkdelist:
    def __init__(self, head= None):
        self.head = head
    
    def delete_at_start(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def del_at_end(self):
       if self.head is None:
            print("List is empty")
            return
       if self.head.next is None:
           self.head = None
           return
       
       current = self.head

       while current.next is not None:
           current = current.next
       current.prev.next = None



    def backwardtraverse(self):
        current = self.head

        while current.next is not None:
            current = current.next
        
        while current is not None:
            print(current.info, end="<-->")
            current = current.prev
        print("none")

    def inser_at_start(self, new_node):
        new_node = Node(new_node)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, info):
        new_node = Node(info)

        if self.head is None:
            self.head = new_node
            return
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert_after(self, target, info):
        current = self.head

        while current is not None:
            if current.info == target:
                new_node = Node(info)

                new_node.next = current.next
                if current.next is not None:
                 current.next.prev = new_node
            
                new_node.prev = current
                current.next = new_node
                return
            current = current.next
        print("node not found") 

    def dispaly(self):
        current = self.head

        while current is not None:
            print(current.info, end="<-->")
            current = current.next
        print("none")

dl = DoublyLinkdelist()

node1 = Node(320)
node2 = Node(220)
node3 = Node(120)
dl.head= node1

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

dl.dispaly()


dl.backwardtraverse()

dl.inser_at_start(420)
dl.dispaly()
      
dl.insert_at_end(20)
dl.dispaly()

dl.insert_after(220,221)
dl.dispaly()

dl.delete_at_start()
dl.dispaly()

dl.del_at_end()
dl.dispaly()

