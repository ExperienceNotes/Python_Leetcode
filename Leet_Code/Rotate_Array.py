nums = [1,2,3,5,7,10]
k = 1
k = k%len(nums)
nums[:k],nums[k:] = nums[len(nums)-k:],nums[:len(nums)-k]
print(nums)