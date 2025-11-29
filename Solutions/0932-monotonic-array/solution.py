class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = all(val1 <= val2 for val1, val2 in pairwise(nums))
        dec = all(val1 >= val2 for val1, val2 in pairwise(nums))
        return inc or dec
