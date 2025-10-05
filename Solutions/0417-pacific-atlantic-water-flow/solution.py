class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        visited1 = [[False] * n for _ in range(m)]
        visited2 = [[False] * n for _ in range(m)]
        queue1: Deque[Tuple[int, int]] = deque()
        queue2: Deque[Tuple[int, int]] = deque()
        directions = (-1, 0, 1, 0, -1)

        for i in range(m):
            queue1.append((i, 0))
            visited1[i][0] = True
            queue2.append((i, n - 1))
            visited2[i][n - 1] = True
        
        for j in range(n):
            queue1.append((0, j))
            visited1[0][j] = True
            queue2.append((m - 1, j))
            visited2[m - 1][j] = True

        def bfs(queue: Deque[Tuple[int, int]], visited: List[List[bool]]) -> None:
            while queue:
                x, y = queue.popleft()
                for dx, dy in pairwise(directions):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and heights[nx][ny] >= heights[x][y]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))


        bfs(queue1, visited1)
        bfs(queue2, visited2)

        return [(i, j) for i in range(m) for j in range(n) if visited1[i][j] and visited2[i][j]]
