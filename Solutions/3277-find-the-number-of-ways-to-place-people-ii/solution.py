class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=(lambda x: (x[0], -x[1])))
        result = 0

        for i, (x1, y1) in enumerate(points):
            max_y = -inf
            for x2, y2 in points[i + 1:]:
                if max_y < y2 <= y1:
                    max_y = y2
                    result += 1

        return result

