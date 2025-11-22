class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)

        @lru_cache
        def dfs(i: int, count: int, lim: bool) -> int:
            if i >= len(s):
                return count

            dig = int(s[i]) if lim else 9
            result = 0
            for j in range(dig + 1):
                result += dfs(i + 1, count + (j == 1), lim and j == dig)
            
            return result
        
        return dfs(0, 0, True)
