class Solution:
    def binaryGap(self, n: int) -> int:
        result, last, current = 0, float('inf'), 0
        while n:
            if n & 1:
                result = max(result, current - last)
                last = current
            current += 1
            n >>= 1
        return result
