class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        max_val = last = current = 0
        for i, val in enumerate(nums):
            current += 1
            if i == len(nums) - 1 or val >= nums[i + 1]:
                max_val = max(max_val, current // 2, min(last, current))
                last, current = current, 0
        
        return max_val >= k
