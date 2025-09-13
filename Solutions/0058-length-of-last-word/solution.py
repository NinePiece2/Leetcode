class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # spl = s.strip().split(" ")
        # return len(spl[-1])

        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1

        j = i
        while j >= 0 and s[j] != " ":
            j -= 1
        
        return i - j
