class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        max_val = 0
        result = 0

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < (dp[j] + 1):
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == (dp[j] + 1):
                        count[i] += count[j]
            if max_val < dp[i]:
                max_val = dp[i]
                result = count[i]
            elif max_val == dp[i]:
                result += count[i]
        
        return result
