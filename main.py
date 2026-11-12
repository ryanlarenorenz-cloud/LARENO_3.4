
from collections import deque

graph = {
    'L': ['A', 'R', 'E'],
    'A': ['R'],
    'R': ['N', 'E'],
    'N': [],
    'E': ['O'],
    'O': []
}

# Breadth-First Search
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print()


# Depth-First Search
def dfs(graph, start):
    visited = set()

    print("DFS Traversal:", end=" ")

    def visit(vertex):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    print()


# Main Program
bfs(graph, 'L')
dfs(graph, 'L')
