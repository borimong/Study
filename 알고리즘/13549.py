
N = 5
K = 17
T = 0

def find_K(N, t):
    
    A = find_K(2*N, t)
    B = find_K(N+1, t+1)
    C = find_K(N-1, t-1)

# K 와 일치하면, 그때의 더 적은 시간을 T 에 저장. 
    if A == K:
        T = min(T, t)
    if B == K:
        T = min(T, t)
    if C == K:
        T = min(T, t)

    return N


find_K(N, T)