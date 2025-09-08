class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i, val1 in enumerate(s, 1):
            for j, val2 in enumerate(t, 1):
                dp[i][j] = dp[i - 1][j]
                if val1 == val2:
                    dp[i][j] += dp[i - 1][j - 1]
        
        return dp[-1][-1]
