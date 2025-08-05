class Solution:
    def reverse(self, x: int) -> int:
        
        result = 0
        MAX, MIN = 2**31 - 1, -2**31
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if result > (MAX - digit) // 10:
                return 0
            result = result * 10 + digit

        return result*sign
