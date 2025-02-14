from itertools import combinations

# [1] 백트래킹(중복조합) -> 100^10 시간초과 아이디어
N, K, P = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
B = list(map(int, input().split())) # [1,2,4,6]
can_B = [i for i in range(1, len(B) + 1)] # 화살의 굵기 [1,2,3,4]
lst = []

for i in range(1, K + 1): 
    for comb in combinations(can_B, i): #[(1),(2),..(1,2),...(1,2,3,4)]
        lst.append(comb)

ans = 1e9 
for l in lst: # 화살의 조합
    total_sum = 0  
    for b in l: # 2두께
        for i in range(N): # 3 # 좌표에다가 화살 꽂음
            for j in range(N): # 3
                for x in range(N): # 0 # 주변칸 탐색
                    for y in range(N): # 0
                        if abs(i - x) + abs(j - y) < b: # 1칸이내에 있는 좌표라면
                            total_sum += graph[x][y] # 칸의 값을 더해
    
    print(total_sum)

    if total_sum == P:
        print(sum(B[b - 1] for b in l))
        ans = min(ans, sum(B[b - 1] for b in l)) 


if ans == 1e9:
    print(-1) 
else:
    print(ans) 