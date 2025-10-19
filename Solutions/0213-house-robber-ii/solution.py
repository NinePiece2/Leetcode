class Solution:
    def rob(self, nums: List[int]) -> int:
        def single_row(nums):
            dp = f = 0
            for num in nums:
                dp, f = max(dp, f), dp + num
            return max(dp, f)
        
        if len(nums) == 1:
            return nums[0]
        
        return max(single_row(nums[1:]), single_row(nums[:-1]))
