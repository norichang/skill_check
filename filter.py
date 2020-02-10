N = int(input())
char = input()

lst = [input() for i in range(N)]
count = 0

for i in lst:
    if char in i:
        print(i)
        count += 1
if count == 0:
    print('None')
