class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if dividend == -(2**31) and divisor == -1:
            return (2**31) - 1

        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor
        result = 0

        while dividend <= divisor:
            val = divisor
            count = 1

            while val >= -(2**31) and dividend <= (val << 1): # << is bitwise shift left
                val <<= 1
                count <<= 1
            dividend -= val
            result += count

        return result if sign else -result
