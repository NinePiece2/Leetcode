class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in map(ord, columnTitle):
            result = result*26 + (char - ord("A")) + 1
        
        return result
