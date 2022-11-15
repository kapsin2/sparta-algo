from collections import deque

c = 11
b = 2

#코니의 위치 변화
#코니는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1만큼 움직입니다
#즉 증가하는 속도가 1초마다 1씩 증가한다는 소리죠.

# 속도
# 1 2 3 4 5 6 7 8 9
# 위치
# 3 4 6 9 13 18 반복문으로 구현가능

# 브라운의 위치 변화는
# B-1, B+1, 2*B
# 2-1 = 1
# 2+1 = 3
# 2*2 = 4

#모든경우의 수를 다 나열해야 한다 == BFS를 써야겠구나

#규칙적 -> 배열, 자유자재 -> 딕셔너리

# 각 시간마다 브라운이 갈 수 있는 위치를 저장하고 싶어요.
#[{}]

def catch_me(cony_loc, brown_loc):
    time = 0;
    queue = deque()
    queue.append((brown_loc, 0))  #위치와 시간을 같이 넣어준다.
    visited = [{}for _ in range(200001)]
    # [{},{},{},{},{}]
    #시간  0   1     -> visited[2] = {0 :True}
    #위치  2   1     -> visited[1] = {1 :True}
    #          3    -> visited[3] = {1 :True}
    #          4    -> visited[4] = {1 :True}
    #
    #
    while cony_loc <= 200000:
        cony_loc += time # 시간만큼 +1 +2 +3 +4
        if time in visited[cony_loc]:
            return time
        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()
            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position,new_time))
            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position,new_time))
            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position,new_time))
        time += 1
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!