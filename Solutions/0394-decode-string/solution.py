class Solution:
    def decodeString(self, s: str) -> str:
        stk1, stk2 = [], []
        num, result = 0, ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stk1.append(num)
                stk2.append(result)
                num = 0
                result = ""
            elif char == "]":
                result = stk2.pop() + result * stk1.pop()
            else:
                result += char
        return result
