class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set_vals = set()
        for val in arr1:
            while val:
                set_vals.add(val)
                val //= 10
        
        result = 0
        for val in arr2:
            while val:
                if val in set_vals:
                    result = max(result, len(str(val)))
                    break
                val //= 10

        return result                
