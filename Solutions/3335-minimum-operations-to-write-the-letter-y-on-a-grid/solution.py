class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count1 = Counter()
        count2 = Counter()

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                a = i == j and i <= n // 2
                b = i + j == n - 1 and i <= n // 2
                c = j == n // 2 and i >= n // 2
                if a or b or c:
                    count1[col] += 1
                else:
                    count2[col] += 1
        return min(n ** 2 - count1[i] - count2[j] for i in range(3) for j in range(3) if i != j)
