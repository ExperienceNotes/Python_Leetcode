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
