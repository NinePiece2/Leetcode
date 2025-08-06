class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            # skip dup nums
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while right > left:
                current = nums[i] + nums[left] + nums[right]

                if abs(current - target) < abs(target - closest):
                    closest = current
                    
                elif current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current
        return closest
