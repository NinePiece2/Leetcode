class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = min(dp[i][k] + dp[k][j] + values[i] * values[j] * values[k]
                    for k in range(i + 1, j)
                )
        return dp[0][-1]
