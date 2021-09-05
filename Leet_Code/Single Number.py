ans = 0
nums = [4,1,2,1,2]
for i in range(len(nums)):
    ans = ans ^ nums[i]
print('ans:',ans)