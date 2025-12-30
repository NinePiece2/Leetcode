class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def checker(i, j):
            if i + 3 > m or j + 3 > n:
                return 0
            set_vals = set()
            row = [0] * 3
            col = [0] * 3
            a = b = 0
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    val = grid[x][y]
                    if val < 1 or val > 9:
                        return 0
                    set_vals.add(val)
                    row[x - i] += val
                    col[y - j] += val
                    if x - i == y - j:
                        a += val
                    if x - i == 2 - y + j:
                        b += val
            
            if len(set_vals) != 9 or a != b:
                return 0
            if any(val != a for val in row) or any(val != a for val in col):
                return 0
            return 1
        
        return sum(checker(i, j) for i in range(m) for j in range(n))
            
