class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # n = len(nums)
        # sums = [[0] * (n - i) for i in range(n)]

        # for j in range(n):
        #     sums[0][j] = nums[j]

        # for i in range(1, n):
        #     for j in range(n - i):
        #         sums[i][j] = sums[i - 1][j] + sums[i - 1][j + 1]
        
        # return sums[-1][-1] % 10

        result = 0
        n = len(nums)
        for i, num in enumerate(nums):
            result += num * comb(n - 1, i)

        return result % 10
