class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(nums1, 1):
            for j, y in enumerate(nums2, 1):
                v = x * y
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], max(0, dp[i - 1][j - 1]) + v)
        return dp[-1][-1]
