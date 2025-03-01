from collections import deque
import sys 

input = sys.stdin.read 

data = input().split("\n")

N, M, V = map(int, data[0].split())

graph = {i: [] for i in range(1, M+1)}

for i in range(1, M+1):
    if data[i].strip():
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)

for key in graph:
    graph[key].sort()

def dfs(v, visited):
    visited.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, visited)


def bfs(start):
    queue = deque([start])
    visited = [start]

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)