class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_table = set(nums)
        result = 0

        for num in hash_table:
            if num - 1 not in hash_table:
                val = num + 1
                while val in hash_table:
                    val += 1
                result = max(result, val - num)

        return result
