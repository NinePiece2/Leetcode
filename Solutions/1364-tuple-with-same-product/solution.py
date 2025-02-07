from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = 0
        hashmap = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                hashmap[prod].append((nums[i], nums[j]))

        for produ, pair in hashmap.items():
            pairs = len(pair)
            if pairs > 1:
                count += pairs * (pairs - 1) * 4
        
        return count
        
