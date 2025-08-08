class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_removed = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[not_removed] = nums[i]
                not_removed += 1

        return not_removed

