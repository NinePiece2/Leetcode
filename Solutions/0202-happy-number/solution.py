class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            val = 0
            while n:
                n, remain = divmod(n, 10)
                val += remain ** 2
            n = val
        
        return n == 1
