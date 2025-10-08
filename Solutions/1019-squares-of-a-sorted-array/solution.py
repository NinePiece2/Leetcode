class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i, num in enumerate(nums):
        #     nums[i] = num ** 2
        
        # return sorted(nums)

        result = []
        i, j = 0, len(nums) - 1
        while j >= i:
            cantidate1 = nums[i] ** 2
            cantidate2 = nums[j] ** 2
            if cantidate1 > cantidate2:
                result.append(cantidate1)
                i += 1
            else:
                result.append(cantidate2)
                j -= 1

        return result[::-1]
