class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        # 建立一個閉包function，計算金額兌換的金幣數量
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
            memo[n] = res
            return memo[n]
        return dp(amount)
