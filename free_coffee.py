import math
N, M = input().split()
price, discount = int(N), int(M)

def calc_price(price, discount):
    init_price = price
    total_price= 0
    while(price > 0):
        price = math.floor(price * (1 - (discount / 100)))
        total_price += price
    print(total_price + init_price)
calc_price(price, discount)
