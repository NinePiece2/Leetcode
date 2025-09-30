class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        looking_for = 1
        result = 0
        i = 0

        while looking_for <= n:
            if i < len(nums) and nums[i] <= looking_for:
                looking_for += nums[i]
                i += 1
            else:
                result += 1
                looking_for *= 2

        return result
