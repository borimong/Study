from collections import deque
import sys

def solve():
    input_line = sys.stdin.readline().strip()
    if not input_line:
        return
    s, t = map(int, input_line.split())
    
    # 같은 경우
    if s == t:
        print("0")
        return
    
    # BFS 상태: (current_value, used_division, operation_sequence)
    # used_division: division (/) 연산을 사용했으면 True, 아니면 False
    queue = deque()
    visited = set()
    queue.append((s, False, ""))
    visited.add((s, False))
    
    while queue:
        value, used, seq = queue.popleft()
        
        # 목표 달성
        if value == t:
            print(seq)
            return
        
        # 연산들을 사전 순(아스키 순서: '*' < '+' < '-' < '/')로 진행하는데,
        # '-' 연산은 항상 0을 만들므로 t가 0이 아니면 쓸모없으므로 제외한다.
        # 1) '*' 연산: value * value
        next_val = value * value
        if value != 1 and next_val <= t and (next_val, used) not in visited:
            visited.add((next_val, used))
            queue.append((next_val, used, seq + "*"))
        # 2) '+' 연산: value + value
        next_val = value + value
        if next_val <= t and (next_val, used) not in visited:
            visited.add((next_val, used))
            queue.append((next_val, used, seq + "+"))
        # 3) '/' 연산: value / value = 1, 단, 이미 division 연산을 사용하지 않은 경우에만.
        if not used and value != 1 and (1, True) not in visited:
            visited.add((1, True))
            queue.append((1, True, seq + "/"))
    
    # 변환 불가능한 경우
    print("-1")
    
if __name__ == '__main__':
    solve()