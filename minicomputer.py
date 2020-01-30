orders_num = int(input())
list = [0, 0]
counter = 0
while counter < orders_num:
    s = input().strip().split(" ")
    
    if s[0] == "SET":
        if s[1] == "1":
            list[0] = int(s[2])
            counter += 1
        if s[1] == "2":
            list[1] = int(s[2])
            counter += 1
    elif s[0] == "ADD":
        list[1] = list[0] + int(s[1])
        counter += 1
    elif s[0] == "SUB":
        list[1] = int(list[0]) - int(s[1])
        counter += 1

print(list[0], list[1])
