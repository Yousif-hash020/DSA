class Root:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
    
    def PreOrder(self,root):

        if root is None:
            return 
        print(root.data,end=" ")
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def PostOrder(self,root):

        if root is None:
            return 
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.data,end=" ")

    def InOrder(self,root):

        if root is None:
            return 
        self.InOrder(root.left)
        print(root.data,end=" ")
        self.InOrder(root.right)
        

root = Root(10)

root.left = Root(5)
root.right = Root(15)

root.left.right = Root(7)
root.left.left = Root(3)

root.right.right = Root(20)
root.right.left = Root(12)


print("\npreorder")
root.PreOrder(root)

print("\ninorder")
root.InOrder(root)


print("\n postorder")
root.PostOrder(root)

        