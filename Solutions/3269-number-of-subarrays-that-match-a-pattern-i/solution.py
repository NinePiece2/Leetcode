class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        result = 0
        def checker(i: int, j: int) -> int:
            return 0 if i == j else (1 if i < j else -1)

        for i in range(len(nums) - len(pattern)):
            result += all(checker(nums[i + k], nums[i + k + 1]) == pat for k, pat in enumerate(pattern))
        
        return result
