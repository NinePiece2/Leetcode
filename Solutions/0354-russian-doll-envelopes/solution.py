class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=(lambda x: (x[0], -x[1])))
        dp = [envelopes[0][1]]

        for _, height in envelopes[1:]:
            if height > dp[-1]:
                dp.append(height)
            else:
                index = bisect_left(dp, height)
                dp[index] = height
        
        return len(dp)
