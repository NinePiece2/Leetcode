class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        modulo = 10**9 + 7

        for i in range(1, n + 1):
            current = i**x
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if current <= j:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - current]) % modulo
        return dp[n][n]
