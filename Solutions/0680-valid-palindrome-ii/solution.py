class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        def check_removal(i, j):
            while j > i:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        while j > i:
            if s[i] != s[j]:
                return check_removal(i + 1, j) or check_removal(i, j - 1)
            i, j = i + 1, j - 1
        
        return True
