class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        n = len(nums)
        if n % 2 == 0:
            sumMedian = (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2

            return sumMedian

        

        return nums[len(nums)//2]
