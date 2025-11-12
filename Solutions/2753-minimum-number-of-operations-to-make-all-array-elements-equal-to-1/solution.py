class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = nums.count(1)
        if count:
            return n - count
        
        result = n + 1
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    result = min(result, j - i + 1)
        
        return -1 if result > n else n + result - 2
