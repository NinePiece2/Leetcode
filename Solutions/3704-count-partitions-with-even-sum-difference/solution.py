class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        result = 0
        for num in nums[:-1]:
            left += num
            right -= num
            result += (left - right) % 2 == 0
        return result
