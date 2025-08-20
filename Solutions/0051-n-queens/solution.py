class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        graph = [["."]* n for _ in range(n)]
        cols = [0] * n
        diag = [0] * (n << 1)
        anti_diag = [0] * (n << 1)

        def dfs(i: int):
            if i == n:
                result.append(["".join(row) for row in graph])
                return
            for j in range(n):
                if cols[j] + diag[j + i] + anti_diag[n - j + i] == 0:
                    graph[i][j] = "Q"
                    cols[j] = diag[j + i] = anti_diag[n - j + i] = 1
                    dfs(i + 1)
                    cols[j] = diag[j + i] = anti_diag[n - j + i] = 0
                    graph[i][j] = "."

        dfs(0)
        return result
