class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        if num < 0:
            return "-" + self.convertToBase7(-num)
        
        result = []
        while num:
            result.append(str(num % 7))
            num //= 7
        
        return "".join(result[::-1])
