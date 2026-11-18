
# Assessment 3.6: DFS Methods in Tree
# Last Name: ARAKAWA

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree using ARAKAWA
root = Node("A0")

root.left = Node("R")
root.right = Node("A1")

root.left.left = Node("A2")
root.left.right = Node("K")

root.right.left = Node("W")
root.right.right = Node("A3")


# PREORDER: Root - Left - Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# INORDER: Left - Root - Right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# POSTORDER: Left - Right - Root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Display Results
print("PREORDER TRAVERSAL:")
preorder(root)

print("\n\nINORDER TRAVERSAL:")
inorder(root)

print("\n\nPOSTORDER TRAVERSAL:")
postorder(root)

print()
