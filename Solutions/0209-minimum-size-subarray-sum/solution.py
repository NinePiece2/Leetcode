class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        li = list(accumulate(nums, initial=0))
        result = n + 1
        for i, val in enumerate(li):
            found = bisect_left(li, val + target)   
            if found <= n:
                result = min(result, found - i)
        return result if result <= n else 0
