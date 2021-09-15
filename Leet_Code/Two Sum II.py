nums = [2,7,11,15]
target = 9
down = 0
top = len(nums) - 1
while top > down:
    ans = nums[down] + nums[top]
    if ans == target:
        print([down+1,top+1])
        break
    elif ans > target:
        top -= 1 
    elif ans < target:
        down += 1
print('if have no any ans print:',[0,0])