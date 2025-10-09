class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        val1 = val2 = val3 = float('-inf')
        for num in nums:
            if num in [val1, val2, val3]:
                continue
            elif num > val1:
                val1, val2, val3 = num, val1, val2
            elif num > val2:
                val2, val3 = num, val2
            elif num > val3:
                val3 = num

        return val3 if val3 != float('-inf') else val1
