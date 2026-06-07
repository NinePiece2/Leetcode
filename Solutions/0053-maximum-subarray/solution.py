class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # result = dp = nums[0]
        # for num in nums[1:]:
        #     dp = max(dp, 0) + num
        #     result = max(result, dp)
        # return result

        result = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum > result:
                result = current_sum
            if current_sum < 0:
                current_sum = 0
                
        return result

        # result = max_ending = nums[0]
        # for i in range(1, len(nums)):
        #     max_ending = max(max_ending + nums[i], nums[i])
        #     result = max(result, max_ending)

        # return result
