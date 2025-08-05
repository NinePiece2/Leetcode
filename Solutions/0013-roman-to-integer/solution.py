class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        previous = 0

        for ch in reversed(s):
            current = roman_numerals[ch]
            if current < previous:
                result -= current
            else:
                result += current
            previous = current
        return result
