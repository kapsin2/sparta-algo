s = "((()))()()"


def is_correct_parenthesis(string):
    ck = 0
    for char in string:
        if ck < 0:
            return False
        elif char == "(":
            ck += 1
        elif char == ")":
            ck -= 1
    if ck == 0:
        return True
    return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!