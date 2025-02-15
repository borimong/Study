from collections import deque
import sys

# 입력 받기 (빠른 입력 사용)
sys.setrecursionlimit(10**6)
data = sys.stdin.read().strip().split("\n")

# 첫 줄: 정점 개수 N, 간선 개수 M, 시작 정점 V
N, M, V = map(int, data[0].split())

# 그래프 초기화 (1-based index)
graph = {i: [] for i in range(1, N + 1)}

# 간선 입력 받기 (양방향 그래프)
for i in range(1, M + 1):
    if data[i].strip():
        a, b = map(int, data[i].split())
        graph[a].append(b)
        graph[b].append(a)

# 각 노드의 연결 리스트를 정렬 (작은 정점부터 방문하기 위해)
for key in graph:
    graph[key].sort()

# DFS (재귀 방식)
def dfs(v, visited):
    visited.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, visited)

# BFS (큐 방식)
def bfs(start):
    queue = deque([start])
    visited = [start]

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited

# 실행
dfs_result = []
dfs(V, dfs_result)
bfs_result = bfs(V)

# 출력
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
