class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        dp = sum(i * val for i, val in enumerate(nums))
        n = len(nums)
        sum_val = sum(nums)
        result = dp
        for i in range(1, n):
            dp = dp + sum_val - n*nums[n - i]
            result = max(result, dp)
        
        return result
