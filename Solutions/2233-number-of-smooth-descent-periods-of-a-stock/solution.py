class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 0
        i, n = 0, len(prices)
        while n > i:
            j = i + 1
            while n > j and prices[j - 1] - prices[j] == 1:
                j += 1
            count = j - i
            result += (count + 1) * count // 2
            i = j
        return result
