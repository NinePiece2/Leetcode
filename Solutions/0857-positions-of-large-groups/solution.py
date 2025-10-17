class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i, n = 0, len(s)
        result = []
        while n > i:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                result.append([i, j - 1])
            i = j
        return result
