class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # m, n = len(coins), amount
        # dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = 0

        # for i, coin in enumerate(coins, 1):
        #     for j in range(n + 1):
        #         dp[i][j] = dp[i - 1][j]
        #         if j >= coin:
        #             dp[i][j] = min(dp[i][j], dp[i][j - coin] + 1)

        # return -1 if dp[-1][-1] == float('inf') else dp[-1][-1]

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[-1]
