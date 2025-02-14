def find_num(A, N):
    # 바뀐 A 는 A 보다 항상 커야 함.  
    for i in range(N - 1, -1, -1):
        if  i == 0:
            return [-1]
        if A[i-1] < A[i]:
            index = 0
            for j in range(N-1, i - 1, -1): # swap 할 놈을 찾기. i-1 보다 오른쪽에 있는 것 중에서 i-1 보다 큰 것 중에 최소
                if A[j] > A[i-1]:
                    index = j
                    break
            A[i-1], A[index] = A[index], A[i-1]
            return A[:i] + sorted(A[i:N])

N = int(input())
A = list(map(int, input().split()))

print(*find_num(A, N))