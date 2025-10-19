class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = dp = nums[0]
        for num in nums[1:]:
            dp = max(dp, 0) + num
            result = max(result, dp)
        return result
