class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        result = 0

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        def dfs(i: int, j: int) -> int:
            sum_val = values[i]
            for l in graph[i]:
                if l != j:
                    sum_val += dfs(l, i)
            nonlocal result
            result += (sum_val % k) == 0
            return sum_val
        
        dfs(0, -1)
        return result
