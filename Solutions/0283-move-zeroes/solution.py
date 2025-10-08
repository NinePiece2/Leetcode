class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_non_zeros = 0
        for i, num in enumerate(nums):
            if num:
                nums[num_non_zeros], nums[i] = nums[i], nums[num_non_zeros]
                num_non_zeros += 1
