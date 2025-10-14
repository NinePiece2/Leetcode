class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # n ^= n // 2
        # return n & (n + 1) == 0

        bin_rep = bin(n)
        return not ("00" in bin_rep or "11" in bin_rep)
