class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result, temp = [], []

        def dfs(i: int, j: int):
            if j == 0:
                if len(temp) == k:
                    result.append(temp[:])
                return
            
            if i > 9 or i > j or len(temp) > k:
                return
            
            temp.append(i)
            dfs(i + 1, j - i)
            temp.pop()
            dfs(i + 1, j)

        dfs(1, n)
        return result
