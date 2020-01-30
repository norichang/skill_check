nums = input().split()
N = int(nums[0])
X = int(nums[1])

bin_N = list(bin(X))
bin_N.pop(0)
bin_N.pop(0)
counter = 1
while counter <= N:
    n = int(input())
    print(bin_N[len(bin_N) - n])
    counter += 1
