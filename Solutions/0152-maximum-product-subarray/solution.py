class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = dp = f = nums[0]
        for num in nums[1:]:
            current_dp, current_f = dp, f
            dp = max(num, current_dp * num, current_f * num)
            f = min(num, current_dp * num, current_f * num)
            result = max(result, dp)
        
        return result
