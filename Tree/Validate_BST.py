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

def isValidBST(root,minimum=float("-inf"),maximum=float("inf")):

        if root is None:
            return True

        if root.value <= minimum or root.value >= maximum:
            return False

        left_valid = isValidBST(
            root.left,
            minimum,
            root.value
        )

        right_valid = isValidBST(
            root.right,
            root.value,
            maximum
        )

        return left_valid and right_valid

   


root = None

root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 20)

inorder(root)


print(isValidBST(root))