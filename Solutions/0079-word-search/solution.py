class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word) - 1:
                return board[i][j] == word[k]
            if board[i][j] != word[k]:
                return False
            
            char = board[i][j]
            board[i][j] = "0"

            for val1, val2 in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + val1, j + val2
                good = 0 <= x < m and 0 <= y < n and board[x][y] != "0"
                if good and dfs(x, y, k + 1):
                    return True
            
            board[i][j] = char
            return False
        
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
