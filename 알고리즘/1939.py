import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_weight = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    max_weight = max(max_weight, C)

start, end = map(int, input().split())

# 주어진 중량 weight로 출발지에서 도착지까지 이동 가능한지 확인하는 함수 (BFS 사용)
def can_transport(weight):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        cur = queue.popleft()
        if cur == end:
            return True
        for nxt, capacity in graph[cur]:
            if not visited[nxt] and capacity >= weight:
                visited[nxt] = True
                queue.append(nxt)
    return False

# 이분 탐색을 이용하여 운반 가능한 최대 중량을 찾음
lo, hi = 1, max_weight
result = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if can_transport(mid):
        result = mid
        lo = mid + 1  # 더 큰 중량으로도 가능하면 범위를 올림
    else:
        hi = mid - 1  # 중량이 너무 크면 줄임

print(result)

import sys
sys.setrecursionlimit(10**6)
from collections import deque

input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_weight = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    max_weight = max(max_weight, C)

start, end = map(int, input().split())

# DFS를 이용하여 주어진 중량 weight로 출발지에서 도착지까지 이동 가능한지 확인하는 함수
def dfs(cur, weight, visited):
    if cur == end:
        return True
    visited[cur] = True
    for nxt, capacity in graph[cur]:
        if not visited[nxt] and capacity >= weight:
            if dfs(nxt, weight, visited):
                return True
    return False

def can_transport(weight):
    visited = [False] * (N + 1)
    return dfs(start, weight, visited)

# 이분 탐색으로 운반 가능한 최대 중량을 찾음
lo, hi = 1, max_weight
result = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if can_transport(mid):
        result = mid
        lo = mid + 1  # 더 큰 중량이 가능한지 확인
    else:
        hi = mid - 1  # 중량이 너무 크면 범위를 줄임

print(result)
