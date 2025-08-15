class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        check1 = n > 0 and (n & (n - 1)) == 0 # Needs to be > 0 and check if 2^2^x
        check2 = n & 0xAAAAAAAA  == 0# bitwise and on every even number 
        return check1 and check2
