class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)

        return [val for val in range(1, len(nums) + 1) if val not in nums_set]
