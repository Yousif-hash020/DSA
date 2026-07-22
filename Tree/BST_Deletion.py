class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)

    if value< root.data:
        root.left = insert(root.left, value)

    if value> root.data:
        root.right = insert(root.right, value)

    return root

def find_min(root):
    current = root

    while current.left is not None:
        current = current.left

    return current

def Delete(root, value):
    if root is  None:
        return None

    if value< root.data:
        root.left = Delete(root.left, value)

    if value > root.data:
        root.right = Delete(root.right, value)

    else:

        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        successor = find_min(root.right)
        root.data =   successor.data

        root.right = Delete(root.right, successor.data)

    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")



root = None

values = [10,5,7,3,12,15,20]

for value in values:
    root = insert(root, value)



inorder(root)
print("\n after delete")
Delete(root,10)
inorder(root)
print("\n post order confirm that 12 is new root ")
postorder(root)




        
            