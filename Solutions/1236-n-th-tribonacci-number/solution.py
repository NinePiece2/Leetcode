class Solution:
    def tribonacci(self, n: int) -> int:
        i, j, k = 0, 1, 1
        for _ in range(n):
            i, j, k = j, k, i + j + k
        return i
