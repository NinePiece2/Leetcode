class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort()
            result = [intervals[0]]
            for start, end in intervals[1:]:
                if result[-1][-1] < start:
                    result.append([start, end])
                else:
                    result[-1][-1] = max(result[-1][-1], end)
            return result

        intervals.append(newInterval)
        return merge(intervals)
