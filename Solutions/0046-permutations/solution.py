class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        values = [0] * n
        result = []
        visited = [False] * n

        def dfs(i: int):
            if i >= n:
                result.append(values[:])
                return

            for j, val in enumerate(nums):
                if not visited[j]:
                    visited[j] = True
                    values[i] = val
                    dfs(i + 1)
                    visited[j] = False
        dfs(0)
        return result
