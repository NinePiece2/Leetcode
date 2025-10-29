class Solution:
    def smallestNumber(self, n: int) -> int:
        val = 1
        while val <= n:
            val <<= 1
        return val - 1
