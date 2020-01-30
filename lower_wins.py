N = int(input())
s = input().split()

c = 0
G_c = 0
P_c = 0

while c < N:
    if s[c] == "G":
        c += 1
        G_c += 1
    elif s[c] == "P":
        c += 1
        P_c += 1
if G_c < P_c:
    print("G")
elif G_c > P_c:
    print("P")
else:
    print("Draw")
