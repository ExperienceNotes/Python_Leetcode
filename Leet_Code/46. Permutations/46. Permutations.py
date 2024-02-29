class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                backtrack(nums, temp)
                temp.pop()
        res = []
        backtrack(nums, [])
        return res
