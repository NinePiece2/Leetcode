class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        @cache
        def dfs(state, val):
            if state == (1 << len(matchsticks)) - 1:
                return True
            for i, num in enumerate(matchsticks):
                if state & (1 << i):
                    continue
                if val + num > div:
                    break
                if dfs(state | (1 << i), (val + num) % div):
                    return True
            return False
            
        div, mod = divmod(sum(matchsticks), 4)
        matchsticks.sort()

        if mod:
            return False
        
        return dfs(0, 0)
