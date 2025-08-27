class Solution:
    def climbStairs(self, n: int) -> int:
        i, j = 0, 1
        for _ in range(n):
            i, j = j, i + j
        
        return j
