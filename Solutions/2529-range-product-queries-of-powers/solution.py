class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []

        while n:
            val = n & -n # Bitwise operation to isolate the rightmost bit
            powers.append(val)
            n -= val

        modulo = 10**9 + 7
        results = []
        for left, right in queries:
            val = 1
            for i in range(left, right + 1):
                val = val * powers[i] % modulo
            results.append(val)
        return results
