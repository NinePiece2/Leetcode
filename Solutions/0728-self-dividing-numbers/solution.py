class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check_num(val: int) -> bool:
            val2 = val
            while val2:
                if val2 % 10 == 0 or val % (val2 % 10):
                    return False
                val2 //= 10
            return True

        return [val for val in range(left, right + 1) if check_num(val)]
