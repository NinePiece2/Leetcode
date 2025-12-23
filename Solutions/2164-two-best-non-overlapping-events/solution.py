class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        dp = [events[-1][2]] * n

        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], events[i][2])

        result = 0
        for _, end, val in events:
            index = bisect_right(events, end, key=lambda x: x[0])
            if index < n:
                val += dp[index]
            result = max(result, val)
        
        return result
