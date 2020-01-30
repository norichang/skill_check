nums = input().split()
a = nums[0]
opt = nums[1]
b = nums[2]
c = nums[4]
answer = 0

if a == "x":

    if opt == "+":
        answer = int(c) - int(b)
    elif opt == "-":
        answer = int(c) + int(b)

if b == "x":
    if opt == "+":
        answer = int(c) - int(a)
    elif opt == "-":
        answer = int(a) - int(c)

if c == "x":
    if opt == "+":
        answer = int(a) + int(b)
    elif opt == "-":
        answer = int(a) - int(b)
       
print(answer)
