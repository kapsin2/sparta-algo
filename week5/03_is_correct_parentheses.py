from collections import deque

balanced_parentheses_string = "()))((()"


# 균형잡힌 괄호 문자열 -> 올바른 괄호문자열
# 올바른 괄호 문자열?

def is_correct_paraentheses(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0


def reverse_parentheses(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string


def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    return u, v


# 1. 입력이 빈문자열인 경우 빈문자열 반환
def change_to_correct_parentheses(string):
    if string == '':
        return ''

    # 2.문자열 w를 두 "균형잡힌 괄호 문자열" u,v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
    # v는 빈문자열이 될 수 있습니다.
    u, v = separate_to_u_v(string)

    # 3.문자열 u가 올바른 괄호 문자열 이라면 문자열 v에대해 1단계부터 다시 수행합니다.
    if is_correct_paraentheses(u):
        return u + change_to_correct_parentheses(v)
    # 4.문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행합니다.
    else:
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_paraentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)
    print('hihihi')

print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
