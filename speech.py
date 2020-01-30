l = input().split()

M = int(l[0])
N = int(l[1])
K = int(l[2])

j = [input() for i in range(K)]

counter = 0
A = 0
B = 0
C = 0
while counter < K:
    if j[counter] == "1":
        A += 1
        counter += 1
        if B >= 1:
            B -= 1
            A += 1
        elif C >= 1:
            C -= 1
            A += 1
    elif j[counter] == "2":
        B += 1
        counter += 1
        if A >= 1:
            A -= 1
            B += 1
        elif C >= 1:
            C -= 1
            B += 1
    elif j[counter] == "3":
        C += 1
        counter += 1
        if B >= 1:
            A -= 1
            C += 1
        elif A >= 1:
            A -= 1
            C += 1

if A > B and A > C:
    print("1")
elif B > A and B > C:
    print("2")
elif C > A and C > B:
    print("3")
elif A == B:
    print("1")
    print("2")
elif B == C:
    print("2")
    print("3")
elif C == A:
    print("1")
    print("2")
