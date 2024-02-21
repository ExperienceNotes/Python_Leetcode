# 322. Coin Change
## Input
* coins: integer array representing coins of different denominations (代表不同硬幣種類)
* amount: integer representing a total amount of money(代表總金額)

## Target
* Return the fewest number of coins that you need to make up that amount.


## Example
* coins = [1, 2, 5]
* amount = 11
* Explanation: 11 = 5 + 5 + 1
* output: 3

## Explane

$$
dp(n) = \begin{cases} 
0 & \text{if } n = 0 \\
-1 & \text{if } n < 0 \\
\min(dp(n - \text{coin}) + 1 | \text{coin} \in \text{coins}) & \text{if } n > 0 
\end{cases}
$$
```python
def dp(n):
    if n == 0:
        return 0
    if n < 0:
        return -1
    res = float('INF')
    for coin in coins:
        subproblem = dn(n - coin)
        res = min(res, 1 + subproblem)
    res = res if res != float('INF') else -1
    return res
```

![Coin Tree](https://github.com/ExperienceNotes/Python_Leetcode/blob/main/Leet_Code/322.%20Coin%20Change/Coin%20Change.JPG?raw=true)

畫出amount=11, coins = {1, 2, 5}時的遞迴樹則會有重複的子問題重複計算，因此使用一個memo計算紀錄已經算過的節點答案。
```python
def dp(n):
    if n in memo:
        return memo[n]
    # 判斷輸入的金額，如果是0代表減完了沒錢了，小於0代表減超過了
    if n == 0:
        return 0
    if n < 0:
        return -1
    res = float('INF')
    # 對於每個金幣進行遞迴計算
    for coin in coins:
        subproblem = dp(n - coin)
        if subproblem == -1:
            contiune
        res = min(res, 1 + subproblem)
    # 計算結束後記得存入節省重複計算時間
    memo[n] = res if res!= float('INF') else -1
    return memo[n]
```
