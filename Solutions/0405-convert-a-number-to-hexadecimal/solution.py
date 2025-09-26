class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        chars = "0123456789abcdef"
        result = []

        for i in range(7, -1, -1):
            val = (num >> (4 * i)) & 0xF
            if val != 0 or result:
                result.append(chars[val])
        
        return "".join(result)
