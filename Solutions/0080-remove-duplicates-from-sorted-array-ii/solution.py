class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 2
        for i in range(2, len(nums)):
            if nums[i - 1] != nums[i] or nums[index-2] != nums[i]:
                nums[index] = nums[i]
                index += 1
                
        return index

