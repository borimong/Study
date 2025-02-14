# 입력 받기
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 방향 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문한 좌표 기록
visited = [[False] * M for _ in range(N)]
max_sum = -float('inf')

def dfs(count, total, start_row, start_col):
    global max_sum
    
    # K개의 칸을 선택했으면 최댓값 갱신
    if count == K:
        max_sum = max(max_sum, total)
        return
    
    # (start_row, start_col)부터 탐색 → 중복 방지
    for i in range(start_row, N):
        for j in range(start_col if i == start_row else 0, M):
            if visited[i][j]:  # 이미 방문한 칸이면 패스
                continue

            # 인접한 칸이 선택되었는지 확인
            is_valid = True
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]:
                    is_valid = False
                    break
            
            if is_valid:
                # 현재 칸 선택
                visited[i][j] = True
                dfs(count + 1, total + grid[i][j], i, j)
                # 백트래킹 (선택 해제)
                visited[i][j] = False

# 백트래킹 시작
dfs(0, 0, 0, 0)

# 결과 출력
print(max_sum)
