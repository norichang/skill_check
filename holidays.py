N = input().split()
holidays = int(N[0])
travelday = int(N[1])
lst = []

for _ in range(holidays):
    lst.extend(input().split())
lst_i = [int(s) for s in lst]
lst_temp = lst_i[1::2]
lst_days = lst_i[0::2]
ave = [0] * (holidays - travelday + 1)
for i in range(holidays - travelday + 1):
    ave[i] = round(sum(lst_temp[i:i + travelday]) / travelday) 
    
print(lst_days[ave.index(min(ave))], lst_days[ave.index(min(ave)) + travelday - 1])
