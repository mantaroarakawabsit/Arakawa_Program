# Graph - ARAKAWA

graph = {
    "A0": ["R", "A1"],
    "R": ["A0", "A2", "K"],
    "A1": ["A0", "W", "A3"],
    "A2": ["R", "K"],
    "K": ["R", "A2", "W"],
    "W": ["A1", "K"],
    "A3": ["A1"]
}


# Breadth-First Search
def BFS(graph, start):
    visited = []
    queue = [start]

    print("BFS Traversal:")

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            print(node, end=" ")

            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    print()


# Depth-First Search
def DFS(graph, node, visited):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            DFS(graph, neighbor, visited)


# Display Results
BFS(graph, "A0")

print("DFS Traversal:")
DFS(graph, "A0", [])
print()