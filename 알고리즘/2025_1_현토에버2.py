import sys
input = sys.stdin.readline

def solve():
    # 1) 입력 받기
    N, K, P = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    B = list(map(int, input().split()))  # B[i] : 굵기 i=1..K의 힘 (인덱스 주의)

    # 2) 각 굵기 i마다 가능한 점수 집합 S_i 구하기
    #    맨해튼 거리 < i 인 영역의 점수를 합산
    #    i는 1부터 K까지로 가정하되, 파이썬 인덱스는 0부터 K-1
    score_candidates = []
    
    for i in range(1, K+1):
        candidate_scores = set()
        for r in range(N):
            for c in range(N):
                # (r, c)를 중심으로 맨해튼 거리 < i인 칸들의 점수 합
                total_score = 0
                for x in range(N):
                    for y in range(N):
                        if abs(x - r) + abs(y - c) < i:
                            total_score += grid[x][y]
                candidate_scores.add(total_score)
        
        # 리스트로 변환
        score_candidates.append(list(candidate_scores))
    
    # 3) DP 배열 초기화
    INF = float('inf')
    # dp[i][p] = 굵기 1..i까지 고려해서 점수 정확히 p를 만드는 데 필요한 최소 힘
    dp = [[INF]*(P+1) for _ in range(K+1)]
    dp[0][0] = 0  # 화살을 하나도 안 썼을 때 점수 0을 만드는 힘 = 0

    # 4) DP 점화
    for i in range(1, K+1):
        # i번째 화살(굵기 i)을 사용하지 않는 경우
        for p in range(P+1):
            dp[i][p] = min(dp[i][p], dp[i-1][p])
        
        # i번째 화살을 사용하는 경우
        for s in score_candidates[i-1]:
            for p in range(P+1):
                if dp[i-1][p] == INF:
                    continue
                new_score = p + s
                if new_score <= P:
                    dp[i][new_score] = min(dp[i][new_score],
                                           dp[i-1][p] + B[i-1])
    
    # 5) 결과 출력
    ans = dp[K][P]
    if ans == INF:
        print(-1)  # 정확히 P를 만들 수 없는 경우
    else:
        print(ans)


# --- 메인에서 solve()를 호출한다고 가정 ---
if __name__ == "__main__":
    solve()
