class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [0] * n
        
        for row in matrix:
            current_dp = [0] * n
            for j, val in enumerate(row):
                left, right = max(0, j - 1), min(n, j + 2)
                current_dp[j] = min(dp[left:right]) + val
            dp = current_dp
        
        return min(dp)
