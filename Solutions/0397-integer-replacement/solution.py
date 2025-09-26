class Solution:
    def integerReplacement(self, n: int) -> int:
        result = 0
        while n != 1:
            if (n & 1) == 0:
                n >>= 1
            elif n != 3 and (n & 3) == 3:
                n += 1
            else:
                n-= 1
            result += 1
        return result
