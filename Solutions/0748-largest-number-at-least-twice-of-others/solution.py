class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = nlargest(2, nums)
        return nums.index(largest[0]) if largest[0] >= largest[1] * 2 else -1
