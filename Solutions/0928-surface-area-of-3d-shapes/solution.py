class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        result = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val:
                    result += 2 + val*4
                    if i:
                        result -= min(val, grid[i - 1][j]) * 2
                    if j:
                        result -= min(val, grid[i][j - 1]) * 2
        return result
