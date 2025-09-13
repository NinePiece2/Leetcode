class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        max_cons = max_vowels = 0
        for char, num_of_occur in count.items():
            if char in "aeiou":
                max_vowels = max(max_vowels, num_of_occur)
            else:
                max_cons = max(max_cons, num_of_occur)
        
        return max_cons + max_vowels
