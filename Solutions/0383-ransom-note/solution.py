class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for letter in ransomNote:
            if count[letter] <= 0:
                return False
            count[letter] -= 1
        
        return True
