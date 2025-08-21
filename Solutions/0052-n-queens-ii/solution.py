class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0
        cols = [False] * n
        diag = [False] * (n << 1)
        anti_diag = [False] * (n << 1)

        def dfs(i: int):
            if i == n:
                nonlocal result
                result += 1
                return
            for j in range(n):
                if cols[j] or diag[j + i] or anti_diag[n - j + i]:
                    continue
                cols[j] = diag[j + i] = anti_diag[n - j + i] = True
                dfs(i + 1)
                cols[j] = diag[j + i] = anti_diag[n - j + i] = False

        dfs(0)
        return result
