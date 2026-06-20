class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0

        for price in prices:
            if min_price < price:
                proft = price - min_price
                best = max(best, proft)
            else:
                min_price = price
        
        return best
