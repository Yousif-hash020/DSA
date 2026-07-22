class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):

        if root is None:
             return Node(value)

        if value< root.value:
            root.left = insert(root.left, value)

        elif value > root.value :
             root.right = insert(root.right, value)

        return root

def find_min(root):
     if root is None:
          return None

     if root.left is None:
          return root.value

     return find_min(root.left)


def inorder(root):
        if root is None:
            return
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)
        

   


root = None

root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 20)

inorder(root)
print("\n minimum ")
print(find_min(root))