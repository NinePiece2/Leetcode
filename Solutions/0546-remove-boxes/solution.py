class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if i > j:
                return 0
            while i < j and boxes[j] == boxes[j - 1]:
                j, k = j - 1, k + 1
            result = dfs(i, j - 1, 0) + ((k + 1)**2)
            for val in range(i, j):
                if boxes[j] == boxes[val]:
                    result = max(result, dfs(val + 1, j - 1, 0) + dfs(i, val, k + 1))
            return result
        
        return dfs(0, n - 1, 0)
