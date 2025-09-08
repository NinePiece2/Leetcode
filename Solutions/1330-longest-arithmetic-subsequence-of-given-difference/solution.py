class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for val in arr:
            dp[val] = dp[val - difference] + 1
        return max(dp.values())
