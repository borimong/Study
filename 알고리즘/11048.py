def max_candies(N, M, candy):
    # DP 테이블 초기화
    dp = [[0] * M for _ in range(N)]
    
    # DP 진행
    for r in range(N):
        for c in range(M):
            # 현재 위치의 사탕 개수
            current = candy[r][c]
            
            # 이전 값들 중 최대값을 선택
            best = 0
            if r > 0: best = max(best, dp[r-1][c])      # 위에서 오는 경우
            if c > 0: best = max(best, dp[r][c-1])      # 왼쪽에서 오는 경우
            if r > 0 and c > 0: best = max(best, dp[r-1][c-1])  # 대각선에서 오는 경우
            
            # 현재 위치의 dp 값 갱신
            dp[r][c] = best + current

    # 최종 결과 출력
    return dp[N-1][M-1]

# 입력 받기
N, M = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_candies(N, M, candy))
