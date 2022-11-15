finding_target = 5
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    current_min = 0
    current_max = len(numbers)-1
    current_guess = (current_max + current_min)//2
    while current_min <= current_max:
        if target == numbers[current_guess]:
            return True
        elif target != numbers[current_guess]:
            current_min = current_guess+1
        current_guess = (current_max+current_min)//2
    current_min = 0
    current_max = len(numbers) - 1
    current_guess = (current_max + current_min) // 2
    while current_min <= current_max:
        if target == numbers[current_guess]:
            return True
        elif target != numbers[current_guess]:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)