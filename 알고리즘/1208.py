from itertools import combinations
from bisect import bisect_left, bisect_right

def count_subsequences_with_sum(n, s, numbers):
    def get_all_sums(nums):
        """부분집합의 합 리스트를 구하는 함수"""
        sums = []
        for size in range(len(nums) + 1):
            for subset in combinations(nums, size):
                sums.append(sum(subset))
        return sums

    # 수열을 반으로 나누기x
    left_part = numbers[:n // 2]
    right_part = numbers[n // 2:]

    # 각 부분에 대해 부분수열의 합 계산
    left_sums = get_all_sums(left_part)
    right_sums = get_all_sums(right_part)

    # 오른쪽 부분의 합을 정렬
    right_sums.sort()

    # 합이 S가 되는 경우의 수 계산
    count = 0
    for left_sum in left_sums:
        target = s - left_sum
        # 오른쪽 부분에서 target에 해당하는 값의 범위 계산
        left_idx = bisect_left(right_sums, target)
        right_idx = bisect_right(right_sums, target)
        count += right_idx - left_idx

    # S == 0인 경우, 공집합을 제외해야 함
    if s == 0:
        count -= 1

    return count

# 입력 받기
n, s = map(int, input().split())
numbers = list(map(int, input().split()))

# 결과 출력
result = count_subsequences_with_sum(n, s, numbers)
print(result)

for i in range(5):
    print(i)