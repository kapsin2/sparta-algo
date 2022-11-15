input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(i+1):
            if array[i-j]> array[i+1-j]:
                array[i-j], array[i+1-j] = array[i+1-j], array[i-j]
            else:
                break     #앞에 두개랑 다르게 더이상 비교할게 없으면 탈출 할수 있다.
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!