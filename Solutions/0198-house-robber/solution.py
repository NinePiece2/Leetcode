class Solution:
    def rob(self, nums: List[int]) -> int:
        skip = rob = 0
        for i in nums:
            skip, rob = max(skip, rob), skip + i
        return max(skip, rob)
