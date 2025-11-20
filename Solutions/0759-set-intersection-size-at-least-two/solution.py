class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], -x[0]))

        result, start, end = 0, -1, -1

        for val1, val2 in intervals:
            if val1 <= start:
                continue
            if val1 > end:
                result += 2
                start, end = val2 - 1, val2
            else:
                result += 1
                start, end = end, val2
        
        return result
