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

![Coin Tree](Leet_Code/322. Coin Change/Coin Change.JPG)
