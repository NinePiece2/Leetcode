class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n)]
        # dp[0][1] = -prices[0]

        # for i in range(1, n):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        
        # return dp[-1][0]

        hold = -prices[0]
        cash = 0
        for price in prices[1:]:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)

        return cash
