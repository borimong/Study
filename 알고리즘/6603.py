from itertools import combinations 

def solution():
    start = -1
    test_case=[]

    while True:
        test_input = list(map(int, input().split()))
        start = int(test_input[0])
        if start == 0:
            break
        test_case.append(test_input)

    for idx, case in enumerate(test_case):
        for comb in combinations(case[1:], 6):
            print(*list(comb))
        if idx != len(test_case) - 1:
            print()


solution()