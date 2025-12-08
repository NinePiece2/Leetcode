class Solution:
    def countTriples(self, n: int) -> int:
        # result = 0
        # for a in range(1, n):
        #     for b in range(1, n):
        #         val = a**2 + b**2
        #         c = int(sqrt(val))
        #         if c <= n and val == c**2:
        #             result += 1
        # return result

        result = 0
        squares = set([i**2 for i in range(1, n + 1)])
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if a**2 + b**2 in squares:
                    result += 2
        return result
