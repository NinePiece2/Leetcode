class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1, s1, b2, s2 = -prices[0], 0, -prices[0], 0
        for price in prices[1:]:
            b1 = max(b1, -price)
            s1 = max(s1, b1 + price)
            b2 = max(b2, s1 - price)
            s2 = max(s2, b2 + price)
        
        return s2
