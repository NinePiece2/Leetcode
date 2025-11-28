class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        sorted_timePoints = sorted(int(val[:2]) * 60 + int(val[3:]) for val in timePoints)
        sorted_timePoints.append(sorted_timePoints[0] + 1440)

        return min(val2 - val1 for val1, val2 in pairwise(sorted_timePoints))
