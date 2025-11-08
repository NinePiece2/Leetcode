class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(val > 0 for row in grid for val in row)
        yz = sum(max(row) for row in grid)
        zx = sum(max(col) for col in zip(*grid))
        return xy + yz + zx
