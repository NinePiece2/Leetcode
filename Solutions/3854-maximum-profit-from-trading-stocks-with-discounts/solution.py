class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            graph[u].append(v)
        
        def dfs(u: int):
            next_val = [[0, 0] for _ in range(budget + 1)]
            for v in graph[u]:
                future_v = dfs(v)
                for j in range(budget, -1, -1):
                    for jv in range(j + 1):
                        for last in (0, 1):
                            val = next_val[j - jv][last] + future_v[jv][last]
                            if val >next_val[j][last]:
                                next_val[j][last] = val

            dp = [[0, 0] for _ in range(budget + 1)]
            price = future[u - 1]
            for j in range(budget + 1):
                for last in (0, 1):
                    cost = present[u - 1] // (last + 1)
                    if j >= cost:
                        dp[j][last] = max(next_val[j][0], next_val[j - cost][1] + (price - cost))
                    else:
                        dp[j][last] = next_val[j][0]
            
            return dp
        
        return dfs(1)[-1][0]
        
