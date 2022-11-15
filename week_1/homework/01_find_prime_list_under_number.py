input = 1000


def find_prime_list_under_number(number):
    prime_list = [2]
    for num in range(number+1):    #index값으로 계산되어서 input값이 포함된 이하로 만들려면 1을 더해줘야 한다.
        ck = 0
        if num <= 1 or num % 2 == 0:     #소수는 2부터 시작하고 2를 제외한 짝수는 소수가 될 수 없다
            continue
        for prime_num in prime_list:       #숫자를 숫자의 제곱근보다 작은 소수로만 나눠봐도 나머지가 0이 되지 않으면 소수인지 알수있다
            if num**(1/2) < prime_num:
                 break
            elif num % prime_num == 0:
                ck += 1
        if ck == 0:
            prime_list.append(num)
    return prime_list


result = find_prime_list_under_number(input)
print(result)