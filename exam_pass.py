data = int(input())
passer = 0
s_score = 0
l_score = 0
total_score = 0


for i in range(data):
    s = input().rstrip().split(' ')
    a = s.pop(0)
    s_i = [int(s) for s in s] 

    total_score = sum(s_i)
    if total_score >= 350:
        if a == "l":
            l_score = s_i[3] + s_i[4]
            if l_score >= 160:
                passer += 1
        elif a == 's':
            s_score = s_i[1] + s_i[2]
            if s_score >= 160:
                passer += 1
print(passer)
