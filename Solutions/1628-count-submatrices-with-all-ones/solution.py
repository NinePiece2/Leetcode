class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        graph = [[0] * n for _ in range(m)]
        result = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    graph[i][j] = 1 if j == 0 else graph[i][j - 1] + 1

        for i in range(m):
            for j in range(n):
                col = inf
                for k in range(i, -1, -1):
                    col = min(col, graph[k][j])
                    result += col
        
        return result
