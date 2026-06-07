class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter({0: 1})
        result = sum_val = 0

        for num in nums:
            sum_val += num  # extend the prefix sum
            result += count[sum_val - k] # how many valid subarrays end here?
            count[sum_val] += 1
        
        return result
