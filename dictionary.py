nums = input().split()
words_num = int(nums[0])
p_words = int(nums[1])
look_for = int(nums[2])
words = input().split()
words.sort()

ans = ((look_for - 1) * p_words)
for i in range(p_words):
    if ans + i >= words_num:
        break
    print(words[ans + i])
