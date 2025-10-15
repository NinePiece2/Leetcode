class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # 10^6 ~ 2^20 (base2) -> 20 digits. Prime numbers 1 to 20 are trivial
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(i.bit_count() in primes for i in range(left, right + 1))
