class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = count = 0

        for num in nums:
            count += num ^ 1
            if count > k:
                count -= nums[left] ^ 1
                left += 1
        
        return len(nums) - left
