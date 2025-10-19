class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        set1 = {}
        set2 = {}

        for a, b in zip(s, t):
            if (a in set1 and set1[a] != b) or (b in set2 and set2[b] != a):
                return False
            set1[a] = b
            set2[b] = a
        
        return True
