class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[float('-inf')] * 3 for _ in range(n + 1)]
        dp[0][0] = 0

        for i, val in enumerate(nums, 1):
            for j in range(3):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][(j - val) % 3] + val)

        return dp[-1][0]
