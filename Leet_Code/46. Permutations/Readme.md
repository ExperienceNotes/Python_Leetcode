# 46. Permutations
## Input
* nums: Given an array nums of distinct integers(給予一個整數數列)

## Target
* Return all the possible permutations.(回傳所有排列組合)


## Example
* nums = [1, 2, 3]
* Output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

## Explane
* 先討論怎樣清況會是找到一組答案，當然是找到的答案(Temp)跟Nums長度相同(終止條件)
```python
if len(temp) == len(nums):
```
* 把Nums每個數字進行遍歷把當下的數字放在答案(Temp)上
* 如果數字已經在答案上就跳過
```python
if nums[i] in temp:
    continue
```
* 沒有的話就加入
```python
temp.append(nums[i])
```
* 接著把nums跟當前的答案(Temp)放進去Recrusive裡面繼續執行
```python
backtrack(nums, temp)
```
* 當執行到Return時把目前的答案(Temp)放在最終的答案(Res)內
```python
res.append(temp[:])
```
* 接著把答案(Temp)，最後一位Pop出來執行下一個可能組合。
```python
temp.pop()
```
* Complete code
```python
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
```
