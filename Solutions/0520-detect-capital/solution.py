class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = sum(char.isupper() for char in word)
        return count == 0 or count == len(word) or (count == 1 and word[0].isupper())
