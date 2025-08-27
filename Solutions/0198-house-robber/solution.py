class Solution:
    def rob(self, nums: List[int]) -> int:
        f = g = 0
        for i in nums:
            f, g = max(f, g), f + i
        return max(f, g)
