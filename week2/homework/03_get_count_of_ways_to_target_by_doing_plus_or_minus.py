numbers = [1, 1, 1, 1, 1]
target_number = 3
way_count = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target,index,sum):
    if index == len(array):
        if sum == target:
            global way_count
            way_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array,target,index+1,
                                                       sum+array[index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array,target,index+1,
                                                       sum-array[index])
    return way_count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number,0,0))  # 5를 반환해야 합니다!