input = "abadabac"

def find_not_repeating_character(string):
    for char in string:
        cnt = 0
        for compare_char in string:
            if char == compare_char:
               cnt += 1
        if cnt == 1:
            return char
    return "_"

result = find_not_repeating_character(input)
print(result)