class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        modulo = 3**19
        result = n > 0 and modulo % n == 0
        return result
