class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removed = 0

        for val in nums:
            if removed == 0 or nums[removed - 1] != val:
                nums[removed] = val
                removed += 1
        return removed
