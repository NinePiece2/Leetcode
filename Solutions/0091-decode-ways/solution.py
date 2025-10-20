class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n
        for i, char in enumerate(s, 1):
            if char != "0":
                dp[i] = dp[i - 1]
            if i > 1 and s[i - 2] != "0" and int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
