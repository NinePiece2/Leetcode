class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        i, j = 0, len(s) - 1
        words = list(s)

        while j > i:
            while j > i and words[i].lower() not in vowels:
                i += 1
            while j > i and words[j].lower() not in vowels:
                j -= 1
            if j > i:
                words[i], words[j] = words[j], words[i]
                i, j = i + 1, j - 1
        
        return "".join(words)
