class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, count = 0, 0, 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
            
        return count
