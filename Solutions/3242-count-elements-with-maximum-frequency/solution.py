class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_vals = max(count.values())
        return sum(x for x in count.values() if x == max_vals)
