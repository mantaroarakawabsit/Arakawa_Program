
# PREORDER TRAVERSAL
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


# Preorder: Root - Left - Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Display Result
print("PREORDER TRAVERSAL:")
preorder(root)
print()
