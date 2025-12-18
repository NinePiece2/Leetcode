class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        profit_prefix_sum = [0] * (n + 1)
        price_prefix_sum = [0] * (n + 1)

        for i, (a, b) in enumerate(zip(prices, strategy), 1):
            profit_prefix_sum[i] = profit_prefix_sum[i - 1] + a * b
            price_prefix_sum[i] = price_prefix_sum[i - 1] + a
        
        result = profit_prefix_sum[-1]
        for i in range(k, n + 1):
            result = max(result, profit_prefix_sum[n] - (profit_prefix_sum[i] - profit_prefix_sum[i - k]) +
                    price_prefix_sum[i] - price_prefix_sum[i - k // 2 ]
                )
                
        return result
