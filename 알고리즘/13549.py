from collections import deque

def find_fastest_time(N, K):
    if N >= K:
        return N - K  # 뒤로만 가는 경우는 -1씩 이동만 하면 됨

    MAX = 100000
    visited = [-1] * (MAX + 1)  # 방문 시간을 저장
    queue = deque([N])
    visited[N] = 0  # 시작 위치

    while queue:
        x = queue.popleft()

        # 순간이동(0초 소요)은 먼저 확인하여 먼저 방문하도록 함
        for next_pos in (x - 1, 2 * x, x + 1):
            if 0 <= next_pos <= MAX and visited[next_pos] == -1:
                if next_pos == 2 * x:
                    visited[next_pos] = visited[x]  # 순간이동은 시간이 증가하지 않음
                    queue.append(next_pos)  # 우선적으로 탐색
                else:
                    visited[next_pos] = visited[x] + 1  # 걷는 경우는 1초 추가
                    queue.append(next_pos)

                if next_pos == K:  # 동생 위치에 도달하면 종료
                    return visited[next_pos]

    return -1  # (문제 조건상 항상 도달 가능하므로 이 경우는 없음)

# 입력 받기
N, K = map(int, input().split())
print(find_fastest_time(N, K))
