import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] : (i, j)에 도달했을 때의 최대 가치 합
dp = [[-10**9] * m for _ in range(n)]
dp[0][0] = grid[0][0]

# 첫 행은 오른쪽으로만 이동 가능
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# 2행부터 n행까지 처리
for i in range(1, n):
    left = [0] * m
    right = [0] * m

    # 왼쪽에서 오른쪽으로 누적
    left[0] = dp[i-1][0] + grid[i][0]
    for j in range(1, m):
        left[j] = max(dp[i-1][j], left[j-1]) + grid[i][j]
    
    # 오른쪽에서 왼쪽으로 누적
    right[m-1] = dp[i-1][m-1] + grid[i][m-1]
    for j in range(m-2, -1, -1):
        right[j] = max(dp[i-1][j], right[j+1]) + grid[i][j]
    
    # 두 방향 중 최댓값 선택
    for j in range(m):
        dp[i][j] = max(left[j], right[j])

# 오른쪽 아래 (N, M)까지의 최대 가치 합 출력
print(dp[n-1][m-1])
