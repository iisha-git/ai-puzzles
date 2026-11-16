from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start, goal = 'A', 'G'

queue = deque([[start]])
visited = {start}

while queue:
    path = queue.popleft()
    node = path[-1]

    if node == goal:
        print("Path:", path)
        break

    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            queue.append(path + [n])
