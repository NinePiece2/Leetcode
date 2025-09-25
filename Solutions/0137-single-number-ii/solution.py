class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return next(key for key, value in count.items() if value == 1)
