nums = input()
p_1 = nums[0]
p_2 = nums[2]
N = int(input())

for i in range(N):
    s = input().rstrip().split(' ')
    c_1 = int(s[0])
    c_2 = int(s[1])

    if int(p_1) > c_1:
        print("High")
    elif int(p_1) < c_1:
        print("Low")
    elif int(p_1) == c_1:
        if int(p_2) < c_2:
            print("High")
        else:
            print("Low")
