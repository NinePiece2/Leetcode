class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1] * (1000) for _ in range(n)]
        result = 0

        for i in range(1, n):
            for k in range(i):
                j = nums[i] - nums[k]
                dp[i][j] = max(dp[i][j], dp[k][j] + 1)
                result = max(result, dp[i][j])
        
        return result
