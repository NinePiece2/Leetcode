class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        result = 0
        while num1 and num2:
            if num1 >= num2:
                result += num1 // num2
                num1 %= num2
            else:
                result += num2 // num1
                num2 %= num1
        return result
