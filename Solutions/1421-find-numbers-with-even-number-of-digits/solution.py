class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(val)) % 2 == 0 for val in nums)
