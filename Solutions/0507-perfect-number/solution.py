class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        sum_val, i = 1, 2
        while i <= num // i:
            if num % i == 0:
                sum_val += i
                if i != num // i:
                    sum_val += num // i
            i += 1
        
        return sum_val == num
