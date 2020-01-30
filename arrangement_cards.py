for i in "4":
    s = input().split()
s.sort(reverse = True)
ans = 10 * int(s[0]) + int(s[2]) + 10 * int(s[1]) + int(s[3])
print(ans)
