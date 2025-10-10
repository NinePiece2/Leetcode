class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for i in range(0, len(s), k * 2):
            chars[i : i + k] = reversed(s[i : i + k])
        return "".join(chars)
