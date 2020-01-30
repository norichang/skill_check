N = int(input())

s = [input() for i in range(N)]
s_i = [int(s) for s in s]
fsteps = s_i[0] - 1
j = 1
steps = 0
while j < N:
    steps = steps + abs(s_i[j] - s_i[j - 1])
    j += 1
print(fsteps + steps)
