class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        result = 1
        sum_val = 1
        for val1, val2 in pairwise(nums):
            sum_val = sum_val + 1 if val1 != val2 else 1
            result += sum_val
        
        return result
