class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        temp = []

        def dfs(i: int):
            if len(temp) == k:
                result.append(temp[:])
                return
            if i > n:
                return
            temp.append(i)
            dfs(i + 1)
            temp.pop()
            dfs(i + 1)
        
        dfs(1)
        return result
