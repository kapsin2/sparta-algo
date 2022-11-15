input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array:  #array 의 길이만큼 아래 식이 실행
        if number == num:  #비교 연산 1번 실행
            return True  #N * 1 = N만큼
    return False

result = is_number_exist(3, input)
print(result)