a = input().split()
init_price = int(a[0])
a_budget = int(a[1])
b_budget = int(a[2])

def auction(init_price, a_budget, b_budget):
    i = 0
    while True:
        if init_price + 10 > a_budget:
                break
        elif init_price + 1000 > b_budget:
                break
        if i % 2 == 0:
            init_price += 10
            i += 1

        else:
            if init_price + 1000 > b_budget:
                break
            elif init_price + 10 > a_budget:
                break
            init_price += 1000
            i += 1


    if i % 2 == 0:
        print('B', init_price)
    else:
        print('A', init_price)

auction(init_price, a_budget, b_budget)
