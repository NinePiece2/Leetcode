class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        values = [0] * n
        result = []
        visited = [False] * n

        def dfs(i: int):
            if i == n:
                result.append(values[:])
                return

            for j, val in enumerate(nums):
                if visited[j] or (j and nums[j] == nums[j - 1] and not visited[j - 1]):
                    continue
                visited[j] = True
                values[i] = val
                dfs(i + 1)
                visited[j] = False
        dfs(0)
        return result
