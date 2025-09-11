class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch.lower() in "aeiou"]
        vowels.sort()
        chars = list(s)
        vowel_loc = 0

        for i, ch in enumerate(chars):
            if ch.lower() in "aeiou":
                chars[i] = vowels[vowel_loc]
                vowel_loc += 1
        
        return "".join(chars)
