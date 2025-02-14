from collections import Counter

def solve():
    N = int(input().strip())
    numbers = [int(input().strip()) for _ in range(N)]
    
    counter = Counter(numbers)
    max_count = max(counter.values())
    
    # 최빈값 후보(등장 횟수가 max_count 인 숫자들) 중 최솟값을 찾음
    answer = min([num for num, cnt in counter.items() if cnt == max_count])
    
    print(answer)

solve()