class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        queue = deque()

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    queue.append((i, j))
                elif val == 1:
                    count += 1

        result = 0
        directions = (-1, 0, 1, 0, -1)
        while queue and count:
            result += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for a, b in pairwise(directions):
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append((x, y))
                        count -= 1
                        if count == 0:
                            return result

        return -1 if count else 0
