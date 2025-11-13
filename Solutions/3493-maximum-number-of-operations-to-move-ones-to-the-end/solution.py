class Solution:
    def maxOperations(self, s: str) -> int:
        result = count = 0
        for i, char in enumerate(s):
            if char == "1":
                count += 1
            elif i and s[i - 1] == "1":
                result += count
        return result
