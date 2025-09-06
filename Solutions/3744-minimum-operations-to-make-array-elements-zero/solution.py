class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def minOps(x: int) -> int:
            ans = 0
            q = i = 1
            while q <= x:
                count = min(q * 4 - 1, x) - q + 1
                ans += count * i
                i += 1
                q *= 4
            return ans

        result = 0
        for l, r in queries:
            sum_min_ops = minOps(r) - minOps(l - 1)
            max_num_ops = minOps(r) - minOps(r - 1)
            result += max((sum_min_ops + 1) // 2, max_num_ops)

        return result
