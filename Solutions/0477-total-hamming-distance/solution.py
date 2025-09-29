class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        max_num = max(nums)
        max_bits = len(format(max_num, 'b'))

        for i in range(max_bits):
            one_bits = sum(x >> i & 1 for x in nums)
            zero_bits = n - one_bits
            result += one_bits * zero_bits

        return result
