class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for val in count(n + 1):
            tmp = val
            counter = [0] * 10

            while tmp:
                tmp, remain = divmod(tmp, 10)
                counter[remain] += 1
            
            if all(num == 0 or i == num for i, num in enumerate(counter)):
                return val
