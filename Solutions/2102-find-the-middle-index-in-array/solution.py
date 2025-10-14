class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, val in enumerate(nums):
            right -= val
            if left == right:
                return i
            left += val
        return -1
