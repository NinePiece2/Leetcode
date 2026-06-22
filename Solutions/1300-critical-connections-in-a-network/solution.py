class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        dfn = [0] * n
        low = [0] * n
        now = 0

        def tarjan(a: int, val: int):
            nonlocal now
            now += 1
            dfn[a] = low[a] = now
            for b in graph[a]:
                if b == val:
                    continue
                if not dfn[b]:
                    tarjan(b, a)
                    low[a] = min(low[a], low[b])
                    if low[b] > dfn[a]:
                        result.append([a, b])
                else:
                    low[a] = min(low[a], dfn[b])

        result = []
        tarjan(0, -1)
        return result
