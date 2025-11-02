class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        directions = (-1, 0, 1, 0, -1)
        dp = [[0] * n for _ in range(m)]
        for i, j in guards:
            dp[i][j] = 2
        for i, j in walls:
            dp[i][j] = 2
        for i, j in guards:
            for val1, val2 in pairwise(directions):
                x, y = i, j
                while 0 <= x + val1 < m and 0 <= y + val2 < n and dp[x + val1][y + val2] < 2:
                    x, y = x + val1, y + val2
                    dp[x][y] = 1
        return sum(val == 0 for row in dp for val in row)
