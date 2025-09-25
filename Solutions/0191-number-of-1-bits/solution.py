class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n -= n & -n
            result += 1
        return result
