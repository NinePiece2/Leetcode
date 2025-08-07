class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = { ')': '(', '}':'{', ']':'['}

        for char in s:
            if char in maps:
                top = stack.pop() if stack else ''
                if maps[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
