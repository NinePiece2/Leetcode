class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(mask: int, val: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                if mask >> i & 1^1:
                    if val + i >= desiredTotal or not dfs(mask | 1 << i, val + i):
                        return True
            return False
        
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        
        return dfs(0, 0)
