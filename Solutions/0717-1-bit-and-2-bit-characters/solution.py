class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # i, n = 0, len(bits)
        # while n - 1> i:
        #     i += bits[i] + 1
        # return i == n - 1

        i = 2
        while i <= len(bits):
            if bits[-1 * i] == 0:
                break
            i += 1

        if i % 2 == 0:
            return True
        return False
