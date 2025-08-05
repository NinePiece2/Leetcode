class Solution:
    def myAtoi(self, s: str) -> int:
        MAX, MIN = 2**31 - 1, -2**31
        s = s.lstrip()
        sign = 1
        current = 0

        if not s:
            return 0

        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            current += 1

        result = 0
        while current < len(s) and s[current].isdigit():
            result = result * 10 + int(s[current])
            current += 1
        result *= sign

        if result < MIN:
            return MIN
        if result > MAX:
            return MAX
        return result
