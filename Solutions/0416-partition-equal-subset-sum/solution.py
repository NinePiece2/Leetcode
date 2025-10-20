class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # m, mod = divmod(sum(nums), 2)

        # # if the sum is odd it can't be split into two subsets
        # if mod:
        #     return False

        # n = len(nums)
        # dp = [[False] * (m + 1) for _ in range(n + 1)]
        # dp[0][0] = True

        # for i, num in enumerate(nums, 1):
        #     for j in range(m + 1):
        #         dp[i][j] = dp[i - 1][j] or (j >= num and dp[i - 1][j - num])
        
        # return dp[-1][-1]

        m, mod = divmod(sum(nums), 2)

        # if the sum is odd it can't be split into two subsets
        if mod:
            return False

        dp = [True] + [False] * m
        for num in nums:
            for j in range(m, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[-1]
