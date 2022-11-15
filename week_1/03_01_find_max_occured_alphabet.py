input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alpha_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for alpha in alpha_array:
        max_occurrence = 0
        max_alphabet = alpha_array[0]
        for char in string:
            occurrence = 0
            if alpha == char:
                occurrence += 1
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alpha
    return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)