class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        for i in range(26):
            char = chr(ord('a') + i)
            left, right = s.find(char), s.rfind(char)
            if right - left > 1:
                result += len(set(s[left + 1 : right]))

        return result
