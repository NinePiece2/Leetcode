class Solution:
    def jump(self, nums: List[int]) -> int:
        result = highest = last = 0
        for i, val in enumerate(nums[:-1]):
            highest = max(highest, i + val)
            if last == i:
                result += 1
                last = highest
        return result
