def get_wood(trees, height):
    return sum(tree - height for tree in trees if tree > height)

def find_max_height(n, m, trees):
    low, high = 0, max(trees)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        wood = get_wood(trees, mid)

        if wood >= m:  # 필요한 나무 이상 확보 가능하면 높이를 올려본다.
            result = mid  # 현재 높이가 가능한 최대값 후보
            low = mid + 1
        else:  # 나무가 부족하면 절단 높이를 낮춰야 한다.
            high = mid - 1
            
    return result

# 입력 받기
n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 결과 출력
print(find_max_height(n, m, trees))