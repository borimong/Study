# 다 해보는 건 10000! 이고, 시간 초과가 남. 
# 규칙을 찾자. 하나 더 작은 게 포인트. 
#뒤에 있는 숫자가 더 크면, 자리를 바꿔도 안됨. => 더 큰 자리를 봐야 함. 더 큰 자리가 기존에 있는 숫자보다 더 작으면, 더 큰 자리로 가고, 더 크면, 그 자리를 그것보다 1 더 작은 수가 그 자리를 대체하고 내림차순 배열 
#뒤에 있는 숫자가 더 작으면, 자리를 바꾸면 됨. 

N = int(input())
numbers = list(map(int, input().split()))

# Step 1: 뒤에서부터 처음으로 감소하는 지점 찾기
idx = -1
for i in range(N - 1, 0, -1):
    if numbers[i - 1] > numbers[i]:
        idx = i - 1
        break

# 사전순으로 가장 처음 순열이면 -1 출력 (감소하는 부분이 없음)
if idx == -1:
    print(-1)
else:
    # Step 2: idx 위치의 값보다 작은 값 중에서 가장 큰 값을 찾기
    for i in range(N - 1, idx, -1):
        if numbers[i] < numbers[idx]:
            numbers[i], numbers[idx] = numbers[idx], numbers[i]
            break

    # Step 3: idx 이후의 부분을 내림차순 정렬
    numbers = numbers[:idx + 1] + sorted(numbers[idx + 1:], reverse=True)

    print(*numbers)





# N = int(input())
# numbers = list(map(int, input().split()))
# arr = []
# answer = []

# for i in range(N):
#     arr.append(numbers[i])

#     if min(arr) == numbers[i] and numbers[i] != 1 and len(arr) > 1:
#         arr.sort(reverse=True)

#         # numbers[i]보다 1 작은 값의 인덱스를 찾기
#         if numbers[i] - 1 in arr:
#             indexOfMinus1 = arr.index(numbers[i] - 1)
#             arr[0], arr[indexOfMinus1] = arr[indexOfMinus1], arr[0]

#         answer = numbers[:N - i - 1] + arr
#         print(answer)
#         break
#     else:
#         arr.sort(reverse=True)
#         answer = numbers[:N - i - 1] + arr
#         print(answer)
#         break

# print(answer)


# N = int(input())
# numbers = list(map(int, input().split()))
# arr = []
# answer = []
# for i in range(N):
#     arr += [numbers[i]]
#     if min(arr) == numbers[i] and numbers[i] != 1 and len(arr) > 1:
#         arr.sort(reverse=True)
#         indexOfMinus1 = arr.index(numbers[i] - 1)
#         arr[0], arr[indexOfMinus1] = arr[indexOfMinus1], arr[0]
#         answer = numbers[N-1-i:N-1] + arr[0:i] 
#         print(
            
#         )
#         print(answer)
#     else :
#         arr.sort(reverse=True) # 자리 바꾸기 내림차순으로
#         # arr 과 numbers 를 합친 다음에 print
#         answer = numbers[N-1-i:N-1] + arr[0:i]
#         print(answer)
#         break

# print(answer)