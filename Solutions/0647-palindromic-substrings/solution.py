class Solution:
    def countSubstrings(self, s: str) -> int:
        result, n = 0, len(s)
        for k in range(n * 2 - 1):
            i, j = k // 2, (k + 1) // 2
            while ~i and j < n and s[i] == s[j]:
                result += 1
                i, j = i - 1, j + 1
        
        return result
