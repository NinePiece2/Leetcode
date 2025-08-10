class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def counter(val: int) -> List[int]:
            count = [0] * 10 # Max digits
            while val:
                val, remain = divmod(val, 10)
                count[remain] += 1
            return count
        
        target = counter(n)
        i = 1
        while i < 10**9:
            if counter(i) == target:
                return True
            i <<= 1 # Bitwise shift left
        return False
