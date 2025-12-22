class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if all (col[j] <= col[i] for col in strs):
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)
