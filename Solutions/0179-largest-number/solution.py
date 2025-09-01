class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        vals = [str(val) for val in nums]
        vals.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        return "0" if vals[0] == "0" else "".join(vals)
