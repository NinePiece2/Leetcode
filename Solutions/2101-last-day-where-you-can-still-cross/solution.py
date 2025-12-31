class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = (-1, 0, 1, 0, -1)
        def checker(val: int) -> bool:
            graph = [[0] * col for _ in range(row)]
            for i, j in cells[:val]:
                graph[i - 1][j - 1] = 1
            q = [(0, j) for j in range(col) if graph[0][j] == 0]
            for x, y in q:
                if x == row - 1:
                    return True
                for a, b in pairwise(directions):
                    dx, dy = x + a, y + b
                    if 0 <= dx < row and 0 <= dy < col and graph[dx][dy] == 0:
                        q.append((dx, dy))
                        graph[dx][dy] = 1
            return False
        
        n = row * col
        left, right = 1, n
        while right > left:
            mid = (left + right + 1) // 2
            if checker(mid):
                left = mid
            else:
                right = mid - 1
        return left
