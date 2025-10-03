class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        priority_queue = []

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heappush(priority_queue, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        directions = (-1, 0, 1, 0, -1)
        result = 0

        while priority_queue:
            height, i, j = heappop(priority_queue)
            for dir1, dir2 in pairwise(directions):
                x, y = i + dir1, j + dir2
                if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y]:
                    result += max(0, height - heightMap[x][y])
                    heappush(priority_queue, (max(height, heightMap[x][y]), x, y))
                    visited[x][y] = True

        return result
