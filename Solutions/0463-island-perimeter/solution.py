class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    result += 4
                    if i < m - 1 and grid[i + 1][j]:
                        result -= 2
                    if j < n - 1 and grid[i][j + 1]:
                        result -= 2
        
        return result
