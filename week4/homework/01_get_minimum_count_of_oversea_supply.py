import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    cnt_way = 0
    index = 0
    max_supply = []
    while stock <= k:    # 재고량이 남은일수보다 크면 ok입니다!!
        while index < len(dates)  and dates[index] <= stock:   #반복문내 인덱스를 초기화 안하고 계속 증가시킨다.(중복append 방지를 위해서)
            #인덱스 범위 0,1,2,3     #현재 재고랑 다음공급날짜를 비교 ex)다음 공급 날짜가 10일인데 재고가 9이면 이미 끝난것임
            heapq.heappush(max_supply, -supplies[index])  #heapq는 기본적으로 최솟값을 구하는것으로 세팅되어있어서 최댓값을 구하려면 * -1을 해준다.
            index +=1
        cnt_way +=1
        stock += -heapq.heappop(max_supply)


    return cnt_way

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))