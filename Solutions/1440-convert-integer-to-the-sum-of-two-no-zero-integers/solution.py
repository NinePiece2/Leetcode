class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num1 in range(1, n):
            num2 = n - num1
            if "0" not in (str(num1) + str(num2)):
                return [num1, num2]
