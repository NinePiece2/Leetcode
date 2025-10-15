class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count = Counter(char.lower() for char in licensePlate if char.isalpha())
        result = None
        for word in words:
            if result and len(word) >= len(result):
                continue
            temp = Counter(word)
            if all(num <= temp[char] for char, num in count.items()):
                result = word
        
        return result
