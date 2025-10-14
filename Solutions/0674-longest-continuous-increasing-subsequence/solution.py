class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = count = 1
        for i, val in enumerate(nums[1:]):
            if nums[i] < val:
                count += 1
                result = max(result, count)
            else:
                count = 1
        return result
