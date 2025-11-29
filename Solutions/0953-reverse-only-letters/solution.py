class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]
        result = []
        for char in s:
            if char.isalpha():
                result.append(letters.pop())
            else:
                result.append(char)
        return "".join(result)
