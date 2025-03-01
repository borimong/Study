from bisect import bisect_left, bisect_right

def solution():
	# 입력
	N, S = map(int, input().split())
	nums = list(map(int, input().split()))
	
	# meet in the middle 구현을 위해 배열을 두 그룹으로 쪼개기
	mid = N // 2
	
	left = nums[:mid]
	right = nums[mid:]
	
	left_sum = []
	right_sum = []
	
	# 왼쪽, 오른쪽 각각의 부분합 구하기
	def find_left_sum(i, sum):
		if i == len(left):
			left_sum.append(sum)
		else:
			find_left_sum(i+1, sum) # 선택하지 않았을 때 
			find_left_sum(i+1, sum + left[i]) # 선택했을 때 
			
	def find_right_sum(i, sum):
		if i == len(right):
			right_sum.append(sum)
		else:
			find_right_sum(i+1, sum) # 선택하지 않았을 때 
			find_right_sum(i+1, sum + right[i]) # 선택했을 때 
			
			
	find_left_sum(0,0)
	find_right_sum(0,0) 
	
	count = 0
	# 이분 탐색으로 합을 만족시키는 경우의 수 구하기 
	left_sum.sort()
	right_sum.sort()
	
	for x in left_sum:
		target = S - x
		left_idx = bisect_left(right_sum, target)
		right_idx = bisect_right(right_sum, target)
		count += (right_idx - left_idx) 
		
	# 예외처리, 공집합이 선택된 경우 
	if S == 0:
		count -= 1 
		
	return count
	
print(solution())