class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # result = duration
        # for atk1, atk2 in pairwise(timeSeries):
        #     result += min(duration, atk2 - atk1)
        # return result

        if len(timeSeries) == 0:
            return 0

        result = 0
        initial = timeSeries[0]
        end = initial + duration

        for time in timeSeries:
            if time >= end:
                result += end - initial
                initial = time
            end = time + duration

        result += end - initial
        return result
