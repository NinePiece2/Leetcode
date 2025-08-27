class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = (1, 1, -1, -1, 1)
        result = 0
        @cache
        def dfs(i: int, j: int, k: int, count: int) -> int:
            x, y = directions[k] + i, directions[k + 1] + j
            target = 2 if grid[i][j] == 1 else (2 - grid[i][j])
            if not 0 <= x < m or not 0 <= y < n or grid[x][y] != target:
                return 0
            
            temp_result = dfs(x, y, k, count)
            if count > 0:
                temp_result = max(temp_result, dfs(x, y, (k + 1) % 4, 0))

            return temp_result + 1
        
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    for k in range(4):
                        result = max(result, dfs(i, j, k, 1) + 1)

        return result
