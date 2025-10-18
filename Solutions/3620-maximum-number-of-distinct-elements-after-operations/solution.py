class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        last = float('-inf')

        for num in nums:
            current = min(num + k, max(num - k, last + 1))
            if current > last:
                result += 1
                last = current
        
        return result
