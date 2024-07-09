class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        value = nums[0]
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != value:
                value = nums[i]
                nums[k] = nums[i]
                k += 1

        return k
