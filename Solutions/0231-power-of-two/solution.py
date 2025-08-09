class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bitwise_opperation = (n & (n - 1)) == 0
        if n > 0:
            return bitwise_opperation
        else:
            return False
