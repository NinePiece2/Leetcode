class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        result = len(intervals)
        last_val = float('-inf')

        for start, end in intervals:
            if last_val <= start:
                result -= 1
                last_val = end
        
        return result
