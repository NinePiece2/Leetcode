class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        sum_val = sum(nums)
        result = last = 0
        for num in nums:
            if num:
                last += num
            elif last * 2 == sum_val:
                result += 2
            elif abs(last * 2 - sum_val) == 1:
                result += 1
        return result
