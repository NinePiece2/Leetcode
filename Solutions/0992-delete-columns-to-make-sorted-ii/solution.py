class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        result = 0
        string_traversal = [False] * (m - 1)

        for j in range(n):
            deletable = False
            for i in range(m - 1):
                if not string_traversal[i] and strs[i][j] > strs[i + 1][j]:
                    deletable = True
                    break
            if deletable:
                result += 1
            else:
                for i in range(m - 1):
                    if not string_traversal[i] and strs[i][j] < strs[i + 1][j]:
                        string_traversal[i] = True
        
        return result
