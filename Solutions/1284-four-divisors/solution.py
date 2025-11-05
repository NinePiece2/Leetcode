class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def checker(val: int) -> int:
            i = 2
            count, sum_val = 2, val + 1
            while i <= val // i:
                if val % i == 0:
                    count += 1
                    sum_val += i
                    if i ** 2 != val:
                        count += 1
                        sum_val += val // i
                i += 1
                if count > 4:
                    return 0
            return sum_val if count == 4 else 0
        
        return sum(checker(val) for val in nums)
