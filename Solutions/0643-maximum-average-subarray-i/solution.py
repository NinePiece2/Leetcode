class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = sum_val = sum(nums[:k])

        for i in range(k, len(nums)):
            sum_val += nums[i] - nums[i - k]
            result = max(result, sum_val)

        return result / k
