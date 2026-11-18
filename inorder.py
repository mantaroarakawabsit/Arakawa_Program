
# INORDER TRAVERSAL
# Last Name: ARAKAWA

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("A0")
root.left = Node("R")
root.right = Node("A1")

root.left.left = Node("A2")
root.left.right = Node("K")

root.right.left = Node("W")
root.right.right = Node("A3")


# Inorder: Left - Root - Right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# Display Result
print("INORDER TRAVERSAL:")
inorder(root)
print()
