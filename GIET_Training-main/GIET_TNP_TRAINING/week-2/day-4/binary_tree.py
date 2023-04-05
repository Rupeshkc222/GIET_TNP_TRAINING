#binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.rigth = None

def in_order(root):
    if root:
        in_order(root.left)
        print(str(root.data) + "->",end = '')
        in_order(root.rigth)
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.rigth)
        print(str(root.data)+"-->",end='')

def pre_order(root):
    if root:
        print(str(root.data) + "->",end = '')
        pre_order(root.left)
        pre_order(root.rigth)

root = Node(1)
root.left = Node(2)
root.rigth = Node(3)
root.left.left = Node(4)
root.left.rigth = Node(5)
print("Inorder traversal")
in_order(root)
print()
print("post order")
post_order(root)
print()
print("Pre order")
pre_order(root)