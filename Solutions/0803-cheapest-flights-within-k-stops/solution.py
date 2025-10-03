class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # graph = defaultdict(list)
        # for source, dest, price in flights:
        #     graph[source].append((dest, price))

        # @cache
        # def dfs(source: int, k: int) -> int:
        #     if source == dst:
        #         return 0
        #     if k <= 0:
        #         return float('inf')

        #     k -= 1
        #     ans = float('inf')
        #     for dest, price in graph[source]:
        #         ans = min(ans, dfs(dest, k) + price)
        #     return ans

        # result = dfs(src, k + 1)

        # return -1 if result == float('inf') else result
        
        # Bellman-Ford approach
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            changed = False
            new_dists = dist[:]

            for source, dest, price in flights:
                if dist[source] != float('inf') and new_dists[dest] > dist[source] + price:
                    new_dists[dest] = dist[source] + price
                    changed = True

            dist = new_dists
            if not changed:
                break
        
        return -1 if dist[dst] == float('inf') else dist[dst]
