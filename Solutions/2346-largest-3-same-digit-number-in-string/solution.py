class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if (char := str(i) * 3) in num:
                return char
        return ""
