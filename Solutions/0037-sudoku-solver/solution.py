class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Backtracking with DFS
        def dfs(val):
            nonlocal good
            if val == len(empty):
                good = True
                return
            i, j = empty[val]

            for l in range(9):
                if row[i][l] == col[j][l] == block[i // 3][j // 3][l] == False:
                    row[i][l] = col[j][l] = block[i // 3][j // 3][l] = True
                    board[i][j] = str(l + 1)
                    dfs(val + 1)
                    row[i][l] = col[j][l] = block[i // 3][j // 3][l] = False
                if good:
                    return 
        
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        empty = []
        good = False

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = int(board[i][j]) - 1 # Zero Indexed
                    row[i][val] = col[j][val] = block[i // 3][j // 3][val] = True

        dfs(0)



