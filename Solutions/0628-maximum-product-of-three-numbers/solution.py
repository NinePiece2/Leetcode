class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest = nlargest(3, nums)
        smallest = nlargest(2, nums, key=lambda x: -x)
        return max(largest[0] * largest[1] * largest[2], largest[0] * smallest[0] * smallest[1])

        # nums.sort()
        # val1 = nums[-1] * nums[-2] * nums[-3]
        # val2 = nums[-1] * nums[0] * nums[1]
        # return max(val1, val2)
