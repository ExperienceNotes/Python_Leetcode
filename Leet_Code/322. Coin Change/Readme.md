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
dp(n) = 
\begin{cases}
\frac{n}{2},  & \text{if $n$ is even} \\
3n+1, & \text{if $n$ is odd}
\end{cases}
$$
