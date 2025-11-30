class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        q = sum(nums) % p
        if q == 0:
            return 0
        last = {0: -1}
        curr = 0
        result = len(nums)
        for i, val in enumerate(nums):
            curr = (curr + val) % p
            target = (curr - q + p) % p
            if target in last:
                result = min(result, i - last[target])
            last[curr] = i
        return -1 if result == len(nums) else result
