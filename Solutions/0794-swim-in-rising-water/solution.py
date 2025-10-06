class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = n ** 2
        p = list(range(m))
        high = [0] * m

        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i, row in enumerate(grid):
            for j, h in enumerate(row):
                high[h] = i * n + j

        directions = (-1, 0, 1, 0, -1)
        for t in range(m):
            div, remain = divmod(high[t], n)
            for dx, dy in pairwise(directions):
                nx, ny = div + dx, remain + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] <= t:
                    p[find(div * n + remain)] = find(nx * n + ny)
            
            if find(0) == find(m - 1):
                return t
        
        return 0
