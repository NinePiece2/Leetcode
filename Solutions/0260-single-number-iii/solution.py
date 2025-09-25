class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_val = reduce(xor, nums)
        val1 = 0
        low_bit = xor_val & -xor_val

        for num in nums:
            if num & low_bit:
                val1 ^= num
        val2 = xor_val ^ val1

        return [val1, val2]
