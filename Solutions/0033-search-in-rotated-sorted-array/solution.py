class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while right > left:
            mid = (left + right) // 2 
            if nums[0] <= nums[mid]: # left side
                if nums[0] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else: # right side
                if nums[mid] < target and target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid

        if nums[left] == target:
            return left
        return -1

