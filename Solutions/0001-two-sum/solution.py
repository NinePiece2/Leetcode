class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        done = {}

        for i, x in enumerate(nums):
            search_val = target - x
            if search_val in done:
                return done[search_val], i

            done[x] = i
