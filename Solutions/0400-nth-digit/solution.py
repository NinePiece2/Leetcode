class Solution:
    def findNthDigit(self, n: int) -> int:
        val, count = 1, 9
        while val * count < n:
            n -= val * count
            val += 1
            count *= 10
        
        num = 10 ** (val - 1) + ((n - 1) // val)
        index = (n - 1) % val
        return int(str(num)[index])
