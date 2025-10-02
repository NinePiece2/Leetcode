class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        result = 1
        visited = {1}

        for _ in range(n):
            result = heappop(heap)
            for val in [2, 3, 5]:
                next_val = result * val
                if next_val not in visited:
                    visited.add(next_val)
                    heappush(heap, next_val)

        return result
