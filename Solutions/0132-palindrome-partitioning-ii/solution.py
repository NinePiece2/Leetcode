class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        graph = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                graph[i][j] = s[i] == s[j] and graph[i + 1][j - 1]
        
        dp = list(range(n))
        for i in range(1, n):
            for j in range(i + 1):
                if graph[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1 if j else 0)
        
        return dp[-1]
