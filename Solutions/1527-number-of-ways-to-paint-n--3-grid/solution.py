class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        count2 = count3 = 6
        for _ in range(n - 1):
            last2, last3 = count2, count3
            count2 = (3 * last2 + 2 * last3) % mod
            count3 = (2 * last2 + 2 * last3) % mod
        return (count2 + count3) % mod
