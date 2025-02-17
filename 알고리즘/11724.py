import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

# 그래프 구성
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 배열
visited = [False] * (n + 1)
connected_components = 0

# BFS 탐색
for i in range(1, n + 1):
    if not visited[i]:  # 방문하지 않은 노드에서 탐색 시작
        bfs(i)
        connected_components += 1

print(connected_components)
