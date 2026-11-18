
# POSTORDER TRAVERSAL
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


# Postorder: Left - Right - Root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Display Result
print("POSTORDER TRAVERSAL:")
postorder(root)
print()
