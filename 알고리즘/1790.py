def find_kth_number(N, K):
    digit = 1
    while K > 0:
        # K는 양수여야 함.
        digitNum = ( 10 ** (digit - 1)) * 9
        if digit * digitNum > K: # 빼야하는 값이 더 커서 K 가 음수로 될 것 같으면, break. 
            break
        K -= digit * digitNum
        digit += 1

    # print(digit)
    # print(digitNum)

    A = K // digit
    B = K % digit
    # print(A)
    # print(B)

    sum = (10 ** (digit - 1) ) - 1
    # print(sum)

    if B == 0:
        C = sum + A 
        if C > N:
            print(-1)
        else:
            print(C % 10)
    elif B != 0:
        C = sum + A + 1
        D = str(C)[B - 1]
        if C > N:
            print(-1)
        else:
            print(D)
        
N , K = map(int, input().split())

find_kth_number(N, K)