current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#북동남서
dr = [-1,0,1,0]
dc = [0,1,0,-1]

#방향전환
def get_d_index_when_rotate_to_left(d):
    return (d+3)%4

#후진
def get_d_index_when_go_back(d):
    return (d+2)%4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleaned = 1 #청소하는 칸의 갯수
    room_map[r][c] = 2
    queue = list([[r,c,d]])

    #큐가 비어지면 종료
    while queue:
        r,c,d = queue.pop(0)     #반복문을 다시 돌때 바로 pop 하기 때문에 queue는 한개를 넘지 않는다.
        temp_d = d

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            #a
            if 0 <= new_r<n and 0 <= new_c<m and room_map[new_r][new_c] == 0: #유효 범위 안에 좌표값이 있으면서 청소가 안되어 있는경우
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r,new_c,temp_d])        #유효하면 queue에 새로운 좌표를 넣는다
                break

            #c
            elif i == 3:
                new_r,new_c = r + dr[get_d_index_when_go_back(d)], c + dc[get_d_index_when_go_back(d)]
                queue.append([new_r,new_c,d])           #queue에 새로운 좌표를 넣는다

                #d
                if room_map[new_r][new_c] == 1:            #갈곳이 없는데 뒤가 벽(1)이면 반환하고 종료
                    return count_of_departments_cleaned

print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
