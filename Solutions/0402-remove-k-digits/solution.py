class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remaining = len(num) - k
        for char in num:
            while k and stack and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
        return "".join(stack[:remaining]).lstrip("0") or "0"
