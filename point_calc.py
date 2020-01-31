N, M = input().split()
prepaid_cash = int(N)
bus_use = int(M)
fee_list = [int(input()) for _ in range(bus_use)]

def calc(prepaid_cash, fee_list):
    points = 0
    for fee in fee_list[0:]:
        if points < fee:
            points += round(fee * 0.1)
            prepaid_cash -= fee
            print(prepaid_cash, points)
        else:
            points -= fee
            print(prepaid_cash, points)

calc(prepaid_cash, fee_list)
