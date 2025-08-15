class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powfunc(val: float, power: int) -> float:
            total = 1
            while power:
                if power & 1:
                    total *= val
                val *= val
                power >>= 1
            return total

        if n >= 0:
            return powfunc(x, n)
        else:
            return 1/ powfunc(x, -n)
