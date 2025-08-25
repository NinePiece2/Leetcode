class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = []

        for k in range (m + n - 1):
            tmp = []
            i = 0 if k < n else k - n +1
            j = k if k < n else n - 1

            while i < m and j >= 0:
                tmp.append(mat[i][j])
                i += 1
                j -= 1
            
            if k % 2 == 0:
                tmp = tmp[::-1]
            result.extend(tmp)
            
        return result
