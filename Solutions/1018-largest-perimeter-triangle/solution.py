class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if (test := nums[i - 1] + nums[i - 2]) > nums[i]:
                return test + nums[i]
        return 0
