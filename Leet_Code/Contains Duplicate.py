nums = [1,2,3,4,5,2]

nums = sorted(nums)
for i in range(0,len(nums)-1):
    if nums[i] == nums[i-1]:
        print('Duplicate')
    else:
        print('not Duplicate')