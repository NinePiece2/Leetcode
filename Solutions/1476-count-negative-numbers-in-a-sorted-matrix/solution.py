class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        result = 0

        while i >= 0 and j < n:
            if grid[i][j] >= 0:
                j += 1
            else:
                result += n - j
                i -= 1
        
        return result
