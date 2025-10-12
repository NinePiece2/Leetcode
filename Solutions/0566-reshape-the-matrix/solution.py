class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]
        for i in range(m * n):
            result[i // c][i % c] = mat[i // n][i % n]
        return result
