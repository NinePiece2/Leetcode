class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = result = 0
        for i in range(2, len(cost) + 1):
            dp, result = result, min(dp + cost[i - 2], result + cost[i - 1])
        return result
