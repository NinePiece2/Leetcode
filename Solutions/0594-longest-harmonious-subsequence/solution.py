class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max((cnt + count[val + 1] for val, cnt in count.items() if count[val + 1]), default=0)
