class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter(num % value for num in nums)
        for i in range(len(nums) + 1):
            if count[i % value] == 0:
                return i
            count[i % value] -= 1

