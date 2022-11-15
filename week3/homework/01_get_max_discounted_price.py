#역정렬을 먼저해서 가장큰 큼액에 가장큰 할인율을 적용해서 더한다.
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def insertion_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(i+1):
            if array[i-j] < array[i+1-j]:
                array[i-j], array[i+1-j] = array[i+1-j], array[i-j]
            else:
                break
    return

def get_max_discounted_price(prices, coupons):
    insertion_sort(prices)
    insertion_sort(coupons)
    i = 0
    j = 0
    amount = 0
    while i < len(prices):
        if j < len(coupons):
            amount += prices[i] * (1 - coupons[j] / 100)
        else:
            amount += prices[i]
        i +=1
        j +=1

    return amount


print(get_max_discounted_price(shop_prices, user_coupons))