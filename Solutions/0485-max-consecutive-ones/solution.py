class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        running_count = 0

        for num in nums:
            if num:
                running_count += 1
                max_cons = max(max_cons, running_count)
            else:
                running_count = 0

        return max_cons
