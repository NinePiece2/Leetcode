class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        result = []
        carry = 0
        while i >= 0 or j >= 0 or carry:
            val1 = 0 if i < 0 else (ord(num1[i]) - ord("0")) 
            val2 = 0 if j < 0 else (ord(num2[j]) - ord("0")) 
            carry, val = divmod(val1 + val2 + carry, 10)
            result.append(str(val))
            i, j = i - 1, j - 1
        return "".join(result[::-1])
        
