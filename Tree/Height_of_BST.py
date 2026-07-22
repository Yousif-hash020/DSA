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

def inorder(root):
        if root is None:
            return
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def Height(root):
     if root is None:
          return 0
     left_height = Height(root.left)     
     right_height = Height(root.right) 

     return 1 + max(left_height, right_height)    

   


root = None

root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 20)

inorder(root)
print("\n")
print(Height(root))