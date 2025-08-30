class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_num = 0
        for i, val in enumerate(nums):
            if max_num < i:
                return False
            max_num = max(max_num, i + val)
        return True
