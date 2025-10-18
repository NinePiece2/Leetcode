class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_val = sum(nums)
        if sum_val < target or (sum_val - target) % 2:
            return 0
        
        n = (sum_val - target) // 2
        dp = [0] * (n + 1)
        dp[0] = 1

        for num in nums:
            for j in range(n, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[-1]
