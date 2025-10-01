class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(k + 1)]

        for j in range(1, k + 1):
            dp[j][1] = -prices[0]

        for price in prices[1:]:
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + price)
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - price)

        return dp[-1][0]
