class Solution:
    def reverseWords(self, s: str) -> str:
        val = s.split()
        result = []
        for word in val:
            result.append(word[::-1])

        return " ".join(result)

        # return " ".join(word[::-1] for word in s.split())
