class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, sum_val: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            sum_val = (sum_val + grid[i][j]) % k
            if i == m - 1 and j == n - 1:
                return int(sum_val == 0)
            return (dfs(i + 1, j, sum_val) + dfs(i, j + 1, sum_val)) % (10**9 + 7)
        
        
        result = dfs(0, 0, 0)
        dfs.cache_clear()
        return result
