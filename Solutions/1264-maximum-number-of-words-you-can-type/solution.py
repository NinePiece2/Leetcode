class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # hash_map = set(brokenLetters)
        counter = 0
        
        for word in text.split():
            for char in word:
                if char in brokenLetters:
                    counter += 1
                    break

        return len(text.split()) - counter
