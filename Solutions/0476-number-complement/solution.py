class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ ((1 << num.bit_length()) - 1) # nums xor ((1 ls num bits) -1)
