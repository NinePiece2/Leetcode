class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        dp = [[-inf] * n for _ in range(n)]
        dp[0][n - 1] = fruits[0][n - 1]

        for i in range(1, n):
            for j in range(i + 1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + fruits[i][j]
                if j + 1 < n:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j + 1] + fruits[i][j])
        
        dp[n - 1][0] = fruits[n - 1][0]
        for j in range(1, n):
            for i in range(j + 1, n):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1]) + fruits[i][j]
                if i + 1 < n:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + fruits[i][j])

        return sum(fruits[i][i] for i in range(n)) + dp[n - 2][n - 1] + dp[n - 1][n - 2]

