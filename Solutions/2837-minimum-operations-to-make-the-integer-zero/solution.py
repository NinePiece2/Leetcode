class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in count(1):
            x = num1 - i * num2
            if x < 0:
                break
            if x.bit_count() <= i <= x:
                return i
        return -1
