class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = j = 0

        for i, num in enumerate(nums):
            count += num ^ 1
            if count > 1:
                count -= nums[j] ^ 1
                j += 1

        return len(nums) - j - 1
