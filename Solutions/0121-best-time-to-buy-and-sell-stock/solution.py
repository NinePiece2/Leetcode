class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0

        for day_price in prices:
            min_price = min(min_price, day_price)
            best = max(best, day_price - min_price)
        
        return best
