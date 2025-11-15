class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        next_val = [n] * (n + 1)
        result = 0
        for i in range(n - 1, -1, -1):
            next_val[i] = next_val[i + 1]
            if s[i] == "0":
                next_val[i] = i

        for i in range(n):
            count_zeros = int(s[i] == "0")
            j = i
            while j < n and count_zeros**2 <= n:
                count_ones = (next_val[j + 1] - i) - count_zeros
                if count_ones >= count_zeros**2:
                    result += min(next_val[j + 1] - j, count_ones - count_zeros**2 + 1)
                j = next_val[j + 1]
                count_zeros += 1
        
        return result
