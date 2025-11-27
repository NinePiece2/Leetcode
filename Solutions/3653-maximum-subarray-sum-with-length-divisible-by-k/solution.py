class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        dp = [float('inf')] * k
        result = float('-inf')
        sum_val = 0
        dp[-1] = 0

        for i, val in enumerate(nums):
            sum_val += val
            result = max(result, sum_val - dp[i % k])
            dp[i % k] = min(sum_val, dp[i % k])
        
        return result
