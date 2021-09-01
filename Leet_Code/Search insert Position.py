def searchinsert(nums,target):
    low,top = 0,len(nums)-1
    mid = (low + top) // 2
    while low<=top:
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            top = mid - 1
        else:
            low = mid + 1
        mid = (low + top) // 2
    return low
nums = [1,3,5,6]
ans = searchinsert(nums,5)
print('Insert in {}'.format(ans))