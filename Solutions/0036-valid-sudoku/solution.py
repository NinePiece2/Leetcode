class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        exists = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue
                num = int(curr) - 1 # Zero Indexing
                k = i // 3 * 3 + j // 3 # Mapping
                if row[i][num] or col[j][num] or exists[k][num]:
                    return False
                row[i][num] = True
                col[j][num] = True
                exists[k][num] = True

        return True
