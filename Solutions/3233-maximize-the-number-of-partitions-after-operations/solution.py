class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        @cache
        def dfs(i: int, current: int, tmp: int) -> int:
            if i >= n:
                return 1
            val = 1 << (ord(s[i]) - ord('a'))

            next_val = current | val
            if next_val.bit_count() > k:
                result = dfs(i + 1, val, tmp) + 1
            else:
                result = dfs(i + 1, next_val, tmp)

            if tmp:
                for j in range(26):
                    next_val = current | (1 << j)
                    if next_val.bit_count() > k:
                        result = max(result, dfs(i + 1, 1 << j, 0) + 1)
                    else:
                        result = max(result, dfs(i + 1, next_val, 0))
            return result
        
        return dfs(0, 0, 1)
