class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        dp.append(nums[0])

        lis = 1
        for i in range(1, n):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                lis += 1
                continue
            
            index = bisect_left(dp, nums[i])
            dp[index] = nums[i]
        
        return lis
