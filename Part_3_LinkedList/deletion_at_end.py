class Node:
    def __init__(self, info, next_node=None):
        self.info = info
        self.next = next_node


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None

    def display(self):
        current = self.head

        while current is not None:
            print(current.info, end=" --> ")
            current = current.next

        print("None")


linked_list = SinglyLinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

linked_list.head = node1

print("Before deletion:")
linked_list.display()

linked_list.delete_at_end()

print("After deletion:")
linked_list.display()