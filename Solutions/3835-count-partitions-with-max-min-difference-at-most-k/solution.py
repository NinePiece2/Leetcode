class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        srted_list = SortedList()
        n = len(nums)
        dp = [1] + [0] * n
        g = [1] + [0] * n
        left = 1
        mod = 10**9 + 7
        for right, num in enumerate(nums, 1):
            srted_list.add(num)
            while srted_list[-1] - srted_list[0] > k:
                srted_list.remove(nums[left - 1])
                left += 1
            dp[right] = (g[right - 1] - (g[left - 2] if left >= 2 else 0) + mod) % mod
            g[right] = (g[right - 1] + dp[right]) % mod

        return dp[-1]
