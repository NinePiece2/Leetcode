class Solution:
    def numSub(self, s: str) -> int:
        result = count = 0
        for char in s:
            if char == "1":
                count += 1
            else:
                count = 0
            result += count
        return result % (10**9 + 7)
