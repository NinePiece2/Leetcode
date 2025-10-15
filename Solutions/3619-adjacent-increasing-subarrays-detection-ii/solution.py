class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        last = current = result = 0
        for i, val in enumerate(nums):
            current += 1
            if i == len(nums) - 1 or val >= nums[i + 1]:
                result = max(result, current // 2, min(last, current))
                last, current = current, 0
        
        return result
