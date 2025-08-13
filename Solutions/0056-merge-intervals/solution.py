class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for left, right in intervals:
            if result[-1][1] < left: # No overlap, this interval's left is more then the last one's right(no overlap) 
                result.append([left, right])
            else:
                result[-1][1] = max(result[-1][1], right) # Overlap, the max of the last interval's right and the 
        return result                                     #  current right is the new interval's right
