class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counter = Counter({0: 1})
        result = temp = 0
        for i in nums:
            temp += i & 1
            result += counter[temp - k]
            counter[temp] += 1
        return result
