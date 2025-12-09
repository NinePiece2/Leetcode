class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = Counter()
        right = Counter(nums)
        result = 0
        mod = 10**9 + 7

        for num in nums:
            right[num] -= 1
            result = (result + left[num * 2] * right[num * 2] % mod) % mod
            left[num] += 1
        
        return result
