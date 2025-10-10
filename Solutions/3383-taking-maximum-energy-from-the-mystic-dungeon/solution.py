class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # n = len(energy)
        # result = float('-inf')

        # for i in range(n - k, n):
        #     j, sum_val = i, 0
        #     while j >= 0:
        #         sum_val += energy[j]
        #         result = max(result, sum_val)
        #         j -= k

        # return result

        dp = energy[:]
        for i in range(len(energy) - k - 1, -1, -1):
            dp[i] += dp[i + k]

        return max(dp)
