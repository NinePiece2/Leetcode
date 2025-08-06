class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # skip dup nums
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while right > left:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    #skip dups for left and right
                    while right > left and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
