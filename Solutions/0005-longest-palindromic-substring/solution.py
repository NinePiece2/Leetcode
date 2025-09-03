class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        k, max_num = 0, 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = False
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j] and max_num < j - i + 1:
                        k, max_num = i, j - i + 1
        
        return s[k : k + max_num]
