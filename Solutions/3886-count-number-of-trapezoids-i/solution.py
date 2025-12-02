class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        count = Counter(point[1] for point in points)
        result = 0
        sum_val = 0
        for val in count.values():
            h_edge = val * (val - 1) // 2
            result = (result + sum_val * h_edge) % (10**9 + 7)
            sum_val += h_edge
        return result
