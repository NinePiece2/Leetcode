class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp1 = [1] * n
        # dp2 = [1] * n
        # result = 1

        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] < nums[j]:
        #             dp1[i] = max(dp1[i], dp2[j] + 1)
        #         elif nums[i] > nums[j]:
        #             dp2[i] = max(dp2[i], dp1[j] + 1)
        #     result = max(result, dp1[i], dp2[i])

        # return result

        inc, dec = 1, 1
        for num1, num2 in pairwise(nums):
            if num2 > num1:
                inc = dec + 1
            elif num2 < num1:
                dec = inc + 1
        return max(inc, dec)
