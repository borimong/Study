# import sys
# sys.setrecursionlimit(10**6)

N, S = map(int,input().split())
numbers = list(map(int, input().split()))

start = 0
end = 0
sum = 0
min_length = float('inf')


while end < N:
    sum += numbers[end]
    end += 1

    while sum >= S:
        sum -= numbers[start]
        min_length = min(min_length, end - start)
        start += 1
        
        # if sum < S:
        #     start -= 1
        #     sum += numbers[start]

    
if min_length == float('inf'):
    print(0)  # 부분합이 S 이상인 구간이 없는 경우
else:
    print(min_length)

# sum += numbers[end]
# end += 1 

# if sum > S:
#     sum -= numbers[start]
#     start += 1

# if sum > S:
#     sum -= numbers[start]
#     start += 1

# sum 이 S 보다 크거나 같을 때까지 end 를 1칸씩 오른쪽으로 이동하고 나서 멈춰. => end 가 끝까지 갈 때까지. 
# sum 이 S 보다 크거나 같을 때까지 start 를 1칸씩 오른쪽으로 이동. sum 이 S 보다 작어지면 안됨. 

# sum += numbers[end]
# end += 1


# 시간 초과 남. (재귀, 반복문)
# arr = []

# def calculate(var):
#     global arr
#     for i in range(len(numbers) - var):
#         temp = 0
#         for j in range(var + 1):
#             temp += numbers[i + j]
#         if temp >= S:
#             arr += [var + 1]
            
#         else:
#             calculate(var + 1)
    

# calculate(1)

# if max(numbers) >= S:
#     print(1)
# elif arr:
#     print(min(arr))


# else:
#     for i in range(len(numbers) - 1):
#         if numbers[i] + numbers[i+1] >= S: 
#             print(2)
       
#     for i in range(len(numbers) - 2):# 달라져야 하는 부분
#         if numbers[i] + numbers[i+1] + numbers[i+2] >= S: # 달라져야 하는 부분
#             print(3) # 달라져야 하는 부분
