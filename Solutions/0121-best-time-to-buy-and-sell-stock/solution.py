class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0

        for day_price in prices:
            if min_price < day_price:
                profit = day_price - min_price
                if profit > best:
                    best = profit
                    
            else:
                min_price = day_price
        
        return best
