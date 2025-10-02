class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        priority_queue = [(0, k -1)]

        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        
        dists = [float('inf')] * n
        dists[k - 1] = 0

        while priority_queue:
            dist, node = heappop(priority_queue)
            if dist > dists[node]:
                continue
            
            for v, weight in graph[node]:
                if (cantidate := dist + weight) < dists[v]:
                    dists[v] = cantidate
                    heappush(priority_queue, (cantidate, v))
        
        result = max(dists)
        return result if result < inf else -1
