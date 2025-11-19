class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        vals = set(nums)
        while original in vals:
            original *= 2
        return original

        
