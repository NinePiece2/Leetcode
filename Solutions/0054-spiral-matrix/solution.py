class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        directions = (0, 1, 0, -1, 0)
        vals = [[False] * n for _ in range(m)]
        i = j = k = 0
        result = []

        for _ in range(m * n):
            result.append(matrix[i][j])
            vals[i][j] = True
            x, y = i + directions[k], j + directions[k + 1]

            if x < 0 or x >= m or y < 0 or y >= n or vals[x][y]:
                k = (k + 1) % 4
            
            i += directions[k]
            j += directions[k + 1]
        
        return result
