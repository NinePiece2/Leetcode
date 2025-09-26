class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        directions = (0, 1, 0, -1, 0)
        i = j = k =0

        for val in range(1, n * n + 1):
            result[i][j] = val
            x, y = i + directions[k], j + directions[k + 1]
            if x < 0 or x >= n or y < 0 or y >= n or result[x][y]:
                k = (k + 1) % 4
            i, j = i + directions[k], j + directions[k + 1]

        return result
