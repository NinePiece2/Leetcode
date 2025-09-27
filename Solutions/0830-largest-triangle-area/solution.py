class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0
        for x1, y1, in points:
            for x2, y2 in points:
                for x3, y3 in points:
                    u1, v1 = x2 - x1, y2 - y1
                    u2, v2 = x3 - x1, y3 - y1
                    tri = abs(u1 * v2 - u2 * v1) / 2
                    result = max(result, tri)

        return result
