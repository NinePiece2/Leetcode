class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [n] * n
        last = float('-inf')
        next_val = float('inf')

        for i, char in enumerate(s):
            if char == c:
                last = i
            result[i] = min(result[i], i - last)
        
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_val = i
            result[i] = min(result[i], next_val - i)
        
        return result
