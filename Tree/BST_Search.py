class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    if value > root.data:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None:
        return False

    if root.data == value:
        return True

    if value< root.data:
        return search(root.left, value)

    return search(root.right, value)

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)



root = None

value = [10,5,7,3,15,12,20]

for values in value:
    root = insert(root, values)



print(search(root, 7))
print(search(root, 25))

inorder(root)

        