# Binary Tree - ARAKAWA

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


# Breadth-First Search
def BFS(root):
    queue = [root]

    print("BFS Traversal:")

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print()


# Depth-First Search
def DFS(node):
    if node:
        print(node.data, end=" ")
        DFS(node.left)
        DFS(node.right)


# Display Results
BFS(root)

print("DFS Traversal:")
DFS(root)
print()