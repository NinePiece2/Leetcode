class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10**9 + 7
        def setter(nums: List[int], k: int):
            nums.extend([1, k])
            nums.sort()
            return {val2 - val1 for val1, val2 in combinations(nums, 2)}
        
        horizontal_set = setter(hFences, m)
        vertical_set = setter(vFences, n)
        result = max(horizontal_set & vertical_set, default=0)
        return result**2 % mod if result else -1
