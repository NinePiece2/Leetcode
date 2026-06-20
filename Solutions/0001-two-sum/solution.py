class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for i, val in enumerate(nums):
            search = target - val
            if search in checked:
                return i, checked[search]

            checked[val] = i
