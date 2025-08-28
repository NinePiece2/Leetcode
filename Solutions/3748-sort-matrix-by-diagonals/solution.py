class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for k in range(n - 2, -1, -1):
            i, j = k, 0
            temp = []
            while i < n and j < n:
                temp.append(grid[i][j])
                i += 1
                j += 1
            temp.sort()

            i, j = k, 0
            while i < n and j < n:
                grid[i][j] = temp.pop()
                i += 1
                j += 1

        for k in range(n - 2, 0, -1):
            i, j = k, n - 1
            temp = []
            while i >= 0 and j >= 0:
                temp.append(grid[i][j])
                i -= 1
                j -= 1
            temp.sort()

            i, j = k, n - 1
            while i >= 0 and j >= 0:
                grid[i][j] = temp.pop()
                i -= 1
                j -= 1
        
        return grid
