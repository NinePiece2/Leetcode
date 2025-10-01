class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1] * n
        temp_arr = sorted((start, i) for i, (start, _) in enumerate(intervals))

        for i, (_, end) in enumerate(intervals):
            j = bisect_left(temp_arr, (end, -inf))
            if j < n:
                result[i] = temp_arr[j][1]
        return result
