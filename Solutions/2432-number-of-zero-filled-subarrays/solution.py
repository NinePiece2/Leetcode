class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = count = 0
        for val in nums:
            if val == 0:
                count += 1
                result += count
            else:
                count = 0
            
        return result
