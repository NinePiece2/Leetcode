class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        for rowStart, colStart, rowEnd, colEnd in queries:
            matrix[rowStart][colStart] += 1
            if rowEnd + 1 < n:
                matrix[rowEnd + 1][colStart] -= 1
            if colEnd + 1 < n:
                matrix[rowStart][colEnd + 1] -= 1
            if rowEnd + 1 < n and colEnd + 1 < n:
                matrix[rowEnd + 1][colEnd + 1] += 1
        
        for i in range(n):
            for j in range(n):
                if i:
                    matrix[i][j] += matrix[i - 1][j]
                if j:
                    matrix[i][j] += matrix[i][j - 1]
                if i and j:
                    matrix[i][j] -= matrix[i - 1][j - 1]
        
        return matrix
