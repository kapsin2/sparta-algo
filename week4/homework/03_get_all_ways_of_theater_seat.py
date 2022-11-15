seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 1
}

def fibo_dynamic_programming(n, fibo_memo): #n개의 자리가 있을때 문제규칙을 따르면 경우의 수는 n번째 피보나치 수열의 수와 일치한다.
    if n in fibo_memo:
        return fibo_memo[n]
    m = fibo_dynamic_programming(n-1 , fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = m
    return m

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    for fixed_seat in fixed_seat_array:    #vip시트 사이의 자리 수를 구해서 피보나치로 경우의 수를 구하고 각각 곱해서 총경우의 수를 계산한다.
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index-current_index,memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo_dynamic_programming(total_count - current_index,memo)
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))